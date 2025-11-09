# 🚀 Deployment Guide for SolarKH Bot

Your bot token: `8314060395:AAHzQECuCSAiyfvMp0SaFzdT6Yfy1yGa8Bs`
Bot username: [@solarkh_bot](https://t.me/solarkh_bot)

## 🆓 Free Hosting Options

### Option 1: Render.com (Recommended - 750 hrs/month free)

#### Setup Steps:

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Push Code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/solarkh-bot.git
   git push -u origin main
   ```

3. **Deploy on Render**
   - Click "New +"
   - Select "Background Worker"
   - Connect your GitHub repository
   - Configure:
     - **Name**: `solarkh-bot`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `python bot.py`
     - **Plan**: Free
   - Click "Create Background Worker"

4. **Bot will be live in ~2 minutes!**

---

### Option 2: Railway.app (500 hrs/month free)

1. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy from GitHub**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway auto-detects Python
   - Click "Deploy"

3. **Bot goes live automatically!**

---

### Option 3: PythonAnywhere (24/7 with limitations)

1. **Create Account**
   - Go to [pythonanywhere.com](https://www.pythonanywhere.com)
   - Sign up for free account

2. **Upload Files**
   - Go to "Files" tab
   - Upload all your bot files
   - Or clone from GitHub

3. **Install Dependencies**
   ```bash
   pip3.10 install --user python-telegram-bot==20.4
   ```

4. **Create Always-On Task**
   - Go to "Tasks" tab
   - Add: `python3.10 /home/yourusername/bot.py`
   - Set to run daily (free accounts can't run 24/7)

---

### Option 4: Heroku (No longer free, but popular)

1. **Install Heroku CLI**
   ```bash
   heroku login
   heroku create solarkh-bot
   git push heroku main
   heroku ps:scale worker=1
   ```

---

## 🔧 Quick Deploy via Render (Easiest)

### Without GitHub:

1. **Zip Your Project**
   - Zip the entire `SolarKH_TelegramBot` folder

2. **Use Render's Git**
   ```bash
   # Install Render CLI
   npm install -g @render/cli
   
   # Login
   render login
   
   # Deploy
   render deploy
   ```

---

## ✅ Verify Deployment

1. Open Telegram and search for `@solarkh_bot`
2. Send `/start`
3. Try: `/quote 300 0.15`

---

## 🐛 Troubleshooting

### Bot not responding:
- Check logs on your hosting platform
- Verify bot token is correct
- Ensure worker/process is running

### Import errors:
- Verify `requirements.txt` is being installed
- Check Python version (needs 3.8+)

### Network timeouts:
- Some networks block Telegram API
- Try deploying to cloud (Render/Railway)

---

## 📊 Monitoring

- **Render**: Dashboard → Your Service → Logs
- **Railway**: Project → Deployments → Logs
- **PythonAnywhere**: Files → Error log

---

## 💡 Tips

1. **Keep bot running 24/7** on Render (best option)
2. **Use environment variables** for sensitive data (optional improvement)
3. **Monitor logs** for errors
4. **Test locally first** with `python bot.py`

---

## 🔄 Update Bot

### On Render/Railway:
```bash
git add .
git commit -m "Update bot"
git push origin main
```
Auto-deploys!

### On PythonAnywhere:
- Re-upload files via Files tab
- Restart task

---

## 🎉 Your Bot is Ready!

Test it now: [t.me/solarkh_bot](https://t.me/solarkh_bot)
