# deploy.ps1 - Quick deployment script for Windows
Write-Host "🚀 SolarKH Bot Deployment Helper" -ForegroundColor Cyan

# Check if git is initialized
if (-not (Test-Path ".git")) {
    Write-Host "`n1️⃣ Initializing Git repository..." -ForegroundColor Yellow
    git init
    git add .
    git commit -m "Initial commit - SolarKH Telegram Bot"
    Write-Host "✅ Git repository created" -ForegroundColor Green
} else {
    Write-Host "✅ Git already initialized" -ForegroundColor Green
}

Write-Host "`n📋 Next Steps:" -ForegroundColor Cyan
Write-Host ""
Write-Host "OPTION 1: Deploy to Render.com (Recommended)" -ForegroundColor Yellow
Write-Host "  1. Go to https://render.com and sign up"
Write-Host "  2. Create a new 'Background Worker'"
Write-Host "  3. Connect this GitHub repo (or upload manually)"
Write-Host "  4. Use these settings:"
Write-Host "     - Build Command: pip install -r requirements.txt"
Write-Host "     - Start Command: python bot.py"
Write-Host "  5. Click 'Create' and wait ~2 minutes"
Write-Host ""

Write-Host "OPTION 2: Deploy to Railway.app" -ForegroundColor Yellow
Write-Host "  1. Go to https://railway.app and sign up"
Write-Host "  2. Click 'New Project' -> 'Deploy from GitHub'"
Write-Host "  3. Select this repository"
Write-Host "  4. Railway auto-deploys!"
Write-Host ""

Write-Host "OPTION 3: Push to GitHub first" -ForegroundColor Yellow
Write-Host "  Run these commands:" -ForegroundColor White
Write-Host "  git remote add origin https://github.com/YOUR_USERNAME/solarkh-bot.git"
Write-Host "  git branch -M main"
Write-Host "  git push -u origin main"
Write-Host ""

Write-Host "📱 Your Bot Info:" -ForegroundColor Cyan
Write-Host "  Username: @solarkh_bot"
Write-Host "  Link: https://t.me/solarkh_bot"
Write-Host "  Token: (already configured in config.py)"
Write-Host ""

Write-Host "✅ Bot is ready to deploy!" -ForegroundColor Green
Write-Host "📖 Read DEPLOYMENT.md for detailed instructions" -ForegroundColor White
