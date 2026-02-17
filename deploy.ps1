# Deploy script for Python Learning App
# Run this to complete the deployment to Streamlit Cloud

Write-Host "`n=== Python Learning App - Deploy to Web ===" -ForegroundColor Cyan
Write-Host ""

# Step 1: Open GitHub to create repo
Write-Host "Step 1: Creating GitHub repository..." -ForegroundColor Yellow
$repoUrl = "https://github.com/new?name=python-learning-app&description=Python+Learning+App+-+Quiz+and+Notebook+Exercises"
Start-Process $repoUrl
Write-Host "  -> Browser opened. Create a NEW repository (leave it empty, no README)."
Write-Host "  -> Copy your GitHub username and repo name."
Write-Host ""

# Step 2: Get user input
$username = Read-Host "Enter your GitHub username"
$reponame = Read-Host "Enter your repo name (or press Enter for 'python-learning-app')"
if ([string]::IsNullOrWhiteSpace($reponame)) { $reponame = "python-learning-app" }

# Step 3: Add remote and push
Write-Host "`nStep 2: Pushing to GitHub..." -ForegroundColor Yellow
Set-Location $PSScriptRoot
git branch -M main 2>$null
git remote remove origin 2>$null
git remote add origin "https://github.com/$username/$reponame.git"
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nStep 3: Deploy on Streamlit Cloud" -ForegroundColor Yellow
    $streamlitUrl = "https://share.streamlit.io/deploy?repository=$username/$reponame&mainFile=app.py"
    Start-Process $streamlitUrl
    Write-Host "  -> Browser opened. Sign in with GitHub and click Deploy!"
    Write-Host "  -> Your app will be at: https://$reponame.streamlit.app" -ForegroundColor Green
} else {
    Write-Host "`nPush failed. Make sure:" -ForegroundColor Red
    Write-Host "  1. You created the repo on GitHub"
    Write-Host "  2. You're logged in (Git may ask for credentials)"
    Write-Host "  3. The repo name matches: $reponame"
}
