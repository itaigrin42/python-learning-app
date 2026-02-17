# Deploy to Streamlit Cloud (Free)

Follow these steps to host your Python Learning App online so you can access it from any browser.

## 1. Create a GitHub account (if you don't have one)

Go to [github.com](https://github.com) and sign up.

## 2. Push your project to GitHub

### Option A: Using GitHub Desktop (easiest)

1. Download [GitHub Desktop](https://desktop.github.com)
2. File → Add Local Repository → select `c:\Users\itaig\Desktop\pyt`
3. If it says "not a Git repository", click "Create a repository"
4. Click "Publish repository" to push to GitHub

### Option B: Using the terminal

```powershell
cd c:\Users\itaig\Desktop\pyt

# Initialize Git (if not already)
git init

# Add all files
git add .
git commit -m "Python Learning App"

# Create a new repo on github.com, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## 3. Deploy on Streamlit Cloud

1. Go to **[share.streamlit.io](https://share.streamlit.io)**
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select your repository, branch (`main`), and set:
   - **Main file path:** `app.py`
5. Click **"Deploy!"**

## 4. Access your app

After a few minutes, you'll get a URL like:
`https://your-app-name.streamlit.app`

Open it in any browser – no terminal needed.

---

**Note:** The app loads your notebooks from the repository. Make sure your `*Questions*.ipynb` and `*h.w*.ipynb` files are included when you push to GitHub.
