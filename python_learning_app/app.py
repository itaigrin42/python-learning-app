"""
Python Learning App - Interactive practice from your Jupyter notebooks.
American-style quiz + coding (no classes, files, or databases in coding section).
"""
import random
import streamlit as st
from pathlib import Path

from .notebook_parser import load_all_exercises, discover_notebooks
from .quiz_questions import QUIZ_QUESTIONS, is_coding_safe_topic
from .code_runner import run_restricted_code, run_draft_code, is_code_allowed, explain_error

# Topics to exclude from the Quiz (per user preference)
QUIZ_EXCLUDED_TOPICS = {"seaborn", "which num"}

# Topics to exclude from Notebook Exercises (per user preference)
NOTEBOOK_EXCLUDED_TOPICS = {"classes", "calc", "files", "seaborn", "loop through files"}


def _is_quiz_topic_excluded(topic: str) -> bool:
    """Exclude Seaborn, Calc*, and Which Num from the quiz."""
    t = topic.strip().lower()
    if t in QUIZ_EXCLUDED_TOPICS:
        return True
    if t.startswith("calc"):
        return True
    if "which num" in t:
        return True
    return False


def _is_notebook_topic_excluded(topic: str) -> bool:
    """Exclude Classes, Calc, Files, Seaborn, loop through files from Notebook Exercises."""
    t = topic.strip().lower()
    return t in NOTEBOOK_EXCLUDED_TOPICS or t.startswith("calc")


def _normalize_topic_for_dedup(topic: str) -> str:
    """Normalize topic for deduplication (DataTypes/Data Types, trailing spaces)."""
    return topic.strip().lower().replace("datatypes", "data types")

# Page config
st.set_page_config(
    page_title="Python Learning App",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a polished look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Outfit:wght@300;400;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
    }
    
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif !important;
        color: #e8e8e8 !important;
    }
    
    .topic-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 1.2rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    .topic-card:hover {
        background: rgba(255,255,255,0.08);
        border-color: #6366f1;
        transform: translateY(-2px);
    }
    
    .exercise-box {
        background: rgba(15,15,35,0.8);
        border: 1px solid rgba(99,102,241,0.3);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .stCodeBlock {
        border-radius: 8px;
        border: 1px solid rgba(99,102,241,0.2);
    }
    
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f23 0%, #1a1a2e 100%);
    }
    
    .success-msg { color: #34d399; }
    .hint-msg { color: #fbbf24; }
</style>
""", unsafe_allow_html=True)


def render_quiz(exercises_by_topic: dict):
    """American-style multiple choice quiz. Includes all topics except Seaborn, Calc, Which Num."""
    st.title("📋 Quiz – Multiple Choice")
    st.caption("Topics: variables, data types, functions, control flow, lists, dicts. No classes, files, or databases.")
    
    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0
    if "quiz_answered" not in st.session_state:
        st.session_state.quiz_answered = {}
    
    def _normalize_topic(t: str) -> str:
        """Normalize topic for deduplication (e.g., 'DataTypes' and 'Data Types' -> same)."""
        s = t.strip().lower().replace("datatypes", "data types")
        return s

    # Build topic list: quiz topics + notebook topics, excluding Seaborn, Calc, Which Num
    # Deduplicate by normalized name to avoid duplicates like "Control Flow"/"Control Flow " and "Variables & DataTypes"/"Variables & Data Types"
    seen_normalized = set()
    topics = []
    all_raw = set(q.topic for q in QUIZ_QUESTIONS) | (set(exercises_by_topic.keys()) if exercises_by_topic else set())
    for t in sorted(all_raw):
        if _is_quiz_topic_excluded(t):
            continue
        key = _normalize_topic(t)
        if key not in seen_normalized:
            seen_normalized.add(key)
            topics.append(t.strip() or t)
    
    topic_filter = st.sidebar.selectbox("Filter by topic", ["All"] + topics)
    
    def _topic_matches(q_topic: str, filter_topic: str) -> bool:
        """Match topics, normalizing whitespace, case, and DataTypes/Data Types."""
        return _normalize_topic(q_topic) == _normalize_topic(filter_topic)
    
    if topic_filter != "All":
        questions_pool = [q for q in QUIZ_QUESTIONS if _topic_matches(q.topic, topic_filter)]
    else:
        # "All" = all quiz questions from non-excluded topics
        questions_pool = [q for q in QUIZ_QUESTIONS if not _is_quiz_topic_excluded(q.topic)]
    
    if not questions_pool:
        st.info(f"No multiple choice questions for **{topic_filter}** yet. Try **Notebook Exercises** mode for coding practice.")
        return
    
    # Show different random questions each time you enter a topic
    if "quiz_last_topic" not in st.session_state:
        st.session_state.quiz_last_topic = None
    
    # Prefer unanswered questions when picking a new set
    def _unanswered_pool():
        return [q for q in questions_pool if f"quiz_{hash(q.question)}" not in st.session_state.quiz_answered]
    
    # How many questions to show: all if 15 or fewer, else 15 random
    n_show = min(15, len(questions_pool)) if len(questions_pool) > 15 else len(questions_pool)
    
    if st.session_state.quiz_last_topic != topic_filter:
        st.session_state.quiz_last_topic = topic_filter
        st.session_state.quiz_empty_reason = None
        unanswered = _unanswered_pool()
        n = min(n_show, len(unanswered)) if unanswered else 0
        questions = random.sample(unanswered, n) if n else []
        st.session_state.quiz_questions = questions
    elif st.sidebar.button("🔄 New questions"):
        unanswered = _unanswered_pool()
        current = st.session_state.get("quiz_questions", [])
        seen = {q.question for q in current}
        # Exclude currently shown questions so we get a fresh set
        candidates = [q for q in unanswered if q.question not in seen]
        if not candidates:
            # All unanswered were just shown
            st.session_state.quiz_questions = []
            st.session_state.quiz_empty_reason = "seen_all"
        else:
            n = min(n_show, len(candidates))
            questions = random.sample(candidates, n)
            st.session_state.quiz_questions = questions
            st.session_state.quiz_empty_reason = None
        st.rerun()
    else:
        questions = st.session_state.get("quiz_questions")
        if questions is None:
            unanswered = _unanswered_pool()
            n = min(n_show, len(unanswered)) if unanswered else 0
            questions = random.sample(unanswered, n) if n else []
            st.session_state.quiz_questions = questions
    
    if not questions:
        reason = st.session_state.get("quiz_empty_reason")
        if reason == "seen_all":
            st.info("You've seen all unanswered questions. Answer some to get more, or switch topics.")
        else:
            st.info("You've answered all questions in this topic. Switch to another topic or try **Notebook Exercises**.")
    else:
        st.session_state.quiz_empty_reason = None
        unanswered_count = len(_unanswered_pool())
        st.caption(f"Showing {len(questions)} of {unanswered_count} unanswered questions (random selection). Switch topic or click **New questions** for a different set.")
    
    labels = ["A", "B", "C", "D"]
    
    for i, q in enumerate(questions):
        key = f"quiz_{hash(q.question)}"  # Stable key per question (survives shuffle)
        answered = key in st.session_state.quiz_answered
        
        st.markdown("---")
        st.markdown(f"**{i + 1}. {q.question}**")
        
        selected = st.radio(
            "Choose your answer:",
            options=range(len(q.options)),
            format_func=lambda j, opts=q.options: f"{labels[j]}. {opts[j]}",
            key=key,
            horizontal=True,
            disabled=answered
        )
        
        if not answered:
            if st.button("Check answer", key=f"submit_{key}"):
                correct = selected == q.correct_index
                st.session_state.quiz_answered[key] = (correct, selected)
                if correct:
                    st.session_state.quiz_score += 1
                st.rerun()
        else:
            correct, _ = st.session_state.quiz_answered[key]
            if correct:
                st.success(f"Correct! {labels[q.correct_index]}. {q.options[q.correct_index]}")
            else:
                st.error(f"Incorrect. The answer is {labels[q.correct_index]}. {q.options[q.correct_index]}")
            if q.explanation:
                st.info(q.explanation)


def render_notebook_exercises(notebook_dir: Path, exercises_by_topic: dict):
    """Notebook-based exercises with filtered coding section."""
    # Deduplicate topics (Data Structures/Data Structures , Variables & Data Types/DataTypes)
    merged: dict[str, list] = {}  # normalized_topic -> exercises
    display_name: dict[str, str] = {}  # normalized_topic -> display name
    for t in exercises_by_topic.keys():
        if _is_notebook_topic_excluded(t):
            continue
        key = _normalize_topic_for_dedup(t)
        if key not in merged:
            merged[key] = []
            display_name[key] = t.strip() or t
        merged[key].extend(exercises_by_topic[t])
    topics = sorted(display_name.values(), key=lambda x: x.lower())
    
    if not topics:
        st.warning("No topics available. Classes, Calc, Files, Seaborn, and loop through files are excluded.")
        return
    
    # Map display name back to normalized key for lookup
    name_to_key = {display_name[k]: k for k in display_name}
    
    st.sidebar.subheader("Topics")
    selected_topic = st.sidebar.selectbox(
        "Choose a topic",
        options=topics,
        format_func=lambda t: f"{t} ({len(merged[name_to_key[t]])} exercises)"
    )
    
    st.sidebar.markdown("---")
    practice_mode = st.sidebar.checkbox("Practice mode (hide solutions)", value=True)
    show_hints = st.sidebar.checkbox("Show example code hints", value=True)
    
    st.title(f"📚 {selected_topic}")
    exercises = merged[name_to_key[selected_topic]]
    
    ex_titles = [f"{e.question_num}. {e.title[:60]}{'...' if len(e.title) > 60 else ''}" 
                 for e in exercises]
    selected_idx = st.selectbox(
        "Select exercise",
        range(len(exercises)),
        format_func=lambda i: ex_titles[i]
    )
    
    ex = exercises[selected_idx]
    
    st.markdown("---")
    st.subheader(f"Exercise {ex.question_num}")
    
    st.markdown(ex.instructions, unsafe_allow_html=True)
    
    if show_hints and ex.hint_code:
        with st.expander("📝 Example / Hint code"):
            st.code(ex.hint_code, language="python")
    
    if ex.solution_code:
        if practice_mode:
            with st.expander("🔓 Reveal solution"):
                st.code(ex.solution_code, language="python")
        else:
            st.subheader("Solution")
            st.code(ex.solution_code, language="python")
    else:
        st.info("No solution code in notebook. Check the hint/example above.")
    
    # Coding section – only for topics that don't use classes, files, or databases
    coding_ok = is_coding_safe_topic(selected_topic)
    
    st.markdown("---")
    st.subheader("✏️ Try it yourself")
    
    if not coding_ok:
        st.info("This topic uses classes, files, or databases. Run your code in the Jupyter notebook instead.")
    else:
        user_code = st.text_area(
            "Write your code here (no classes, files, or databases)",
            height=150,
            placeholder="# Variables, functions, loops, lists, dicts only.\n# Example: x = 5; print(x * 2)"
        )
        
        if st.button("▶ Run Code", type="primary"):
            if not user_code or not user_code.strip():
                st.warning("Please write some code first.")
            else:
                allowed, reason = is_code_allowed(user_code)
                if not allowed:
                    st.error(reason)
                else:
                    success, output, error = run_restricted_code(user_code)
                    if success:
                        if output:
                            st.code(output, language=None)
                        st.success("Code executed successfully!")
                    else:
                        explanation = explain_error(error)
                        st.error(explanation, icon="⚠️")
                        st.caption(f"Technical details: {error}")
                        if output:
                            st.code(output, language=None)


def render_draft():
    """Draft mode: write and run code with pandas, matplotlib, seaborn, etc."""
    st.title("✏️ Draft")
    st.caption("Write and run Python code. Includes pandas, numpy, matplotlib, seaborn, and more.")
    
    user_code = st.text_area(
        "Write your code here",
        height=250,
        placeholder="""import pandas as pd
import matplotlib.pyplot as plt

# Your code here
df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
plt.plot(df['x'], df['y'])
plt.show()"""
    )
    
    if st.button("▶ Run Code", type="primary", key="draft_run"):
        if not user_code or not user_code.strip():
            st.warning("Please write some code first.")
        else:
            with st.spinner("Running..."):
                success, output, error = run_draft_code(user_code, st)
            if success:
                if output:
                    st.code(output, language=None)
                st.success("Code executed successfully!")
            else:
                explanation = explain_error(error)
                st.error(explanation, icon="⚠️")
                st.caption(f"Technical details: {error}")
                if output:
                    st.code(output, language=None)


def main():
    app_dir = Path(__file__).parent
    notebook_dir = app_dir.parent
    
    st.sidebar.title("🐍 Python Learning")
    st.sidebar.markdown("---")
    
    mode = st.sidebar.radio(
        "Mode",
        ["📋 Quiz (Multiple Choice)", "📚 Notebook Exercises", "✏️ Draft"],
        help="Quiz: MC questions. Notebook: exercises. Draft: write & run any code."
    )
    
    if "Draft" in mode:
        render_draft()
        return
    
    # Notebook Exercises load from app's built-in exercises (not user's notebooks)
    notebook_exercises_dir = app_dir / "notebook_exercises"
    with st.spinner("Loading exercises..."):
        exercises_by_topic = load_all_exercises(notebook_exercises_dir) or {}
    
    if "Quiz" in mode:
        render_quiz(exercises_by_topic)
        return
    
    # Notebook exercises (built-in only)
    st.sidebar.markdown("**Practice exercises**")
    
    if not exercises_by_topic:
        st.error("No exercises found.")
        return
    
    render_notebook_exercises(notebook_exercises_dir, exercises_by_topic)
    
    st.sidebar.markdown("---")
    st.sidebar.caption(f"{len(discover_notebooks(notebook_exercises_dir))} topic(s)")


if __name__ == "__main__":
    main()
