# 🚀 Deploy to PythonAnywhere - Quick Guide

## ✅ Everything is Ready!

All code has been pushed to GitHub:
**Repository:** https://github.com/chhany007/solarkh_bot_new

---

## 📋 Step-by-Step Deployment

### **Step 1: Login to PythonAnywhere**
Go to: https://www.pythonanywhere.com
Login to your account

---

### **Step 2: Open Bash Console**
1. Click on "Consoles" tab
2. Click "Bash" to open a new console

---

### **Step 3: Stop Old Bot (if running)**
```bash
# Kill any running bot processes
pkill -f bot.py

# Wait a few seconds
sleep 5

# Verify nothing is running
ps aux | grep bot.py
```

---

### **Step 4: Update Code from GitHub**
```bash
# Go to your bot directory
cd ~/solarkh_bot_new

# Pull latest changes
git pull origin main

# Verify files updated
ls -la
```

**You should see:**
- ✅ `data/solar_education.json` (NEW)
- ✅ `utils/product_viewer.py` (NEW)
- ✅ `assets/` folder (NEW)
- ✅ Updated `bot.py`
- ✅ Updated `languages.py`
- ✅ Updated `data/components.json`

---

### **Step 5: Check Dependencies**
```bash
# Make sure all packages are installed
pip3.10 install --user python-telegram-bot==20.4

# Verify installation
python3.10 -c "import telegram; print(telegram.__version__)"
```

Should show: `20.4`

---

### **Step 6: Test Bot Quickly**
```bash
# Quick test (will show any errors)
python3.10 bot.py
```

**If you see:**
```
✅ SolarKH Bot started successfully!
Press Ctrl+C to stop the bot.
```

**Then press `Ctrl+C` to stop and continue to Step 7.**

**If you see errors**, check:
- Bot token in `config.py`
- All files present
- Python version

---

### **Step 7: Start Bot in Background**
```bash
# Start bot with nohup (keeps running after you logout)
nohup python3.10 bot.py > bot.log 2>&1 &

# Get the process ID
echo $!
```

**Save that process ID!**

---

### **Step 8: Verify Bot is Running**
```bash
# Check if bot process is running
ps aux | grep bot.py

# Watch the log file (Ctrl+C to exit)
tail -f bot.log
```

**You should see:**
```
✅ SolarKH Bot started successfully!
Bot started
```

---

### **Step 9: Test in Telegram**

Open Telegram and test:

1. **Start Bot:**
   ```
   /start
   ```
   ✅ Should see logo and welcome message

2. **Test Products:**
   ```
   /products
   ```
   ✅ Should see logo and product categories

3. **Test Education:**
   ```
   /learn
   ```
   ✅ Should see logo and lesson topics

4. **Test Quote:**
   ```
   /quote 800 0.18
   ```
   ✅ Should get instant quote

5. **Test Language:**
   - Click "🌐 Language"
   - Select Khmer
   ✅ Should see logo and Khmer interface

---

## 🔧 Troubleshooting

### **Bot Not Responding?**

**Check if running:**
```bash
ps aux | grep bot.py
```

**Check logs:**
```bash
tail -50 bot.log
```

**Restart bot:**
```bash
pkill -f bot.py
nohup python3.10 bot.py > bot.log 2>&1 &
```

---

### **409 Conflict Error?**

This means another instance is running somewhere.

**Solution:**
```bash
# Stop ALL instances
pkill -f bot.py

# Wait 30 seconds
sleep 30

# Delete webhook (if any)
python3.10 -c "
from telegram import Bot
import asyncio
bot = Bot('YOUR_BOT_TOKEN')
asyncio.run(bot.delete_webhook(drop_pending_updates=True))
"

# Wait another 30 seconds
sleep 30

# Start fresh
nohup python3.10 bot.py > bot.log 2>&1 &
```

---

### **Logo Not Showing?**

The logo URL in `config.py` points to GitHub. If logo doesn't show:

**Option 1: Use direct image URL**
Edit `config.py`:
```python
LOGO_URL = "https://i.imgur.com/YOUR_IMAGE.png"
```

**Option 2: Upload to GitHub**
1. Add `logo.png` to `assets/` folder locally
2. Commit and push
3. Logo will work automatically

**Option 3: Disable logo temporarily**
The bot has fallback - it will work without logo!

---

### **Import Errors?**

```bash
# Reinstall dependencies
pip3.10 install --user python-telegram-bot==20.4

# Check Python version
python3.10 --version
```

---

## 📊 Monitor Bot

### **Check if running:**
```bash
ps aux | grep bot.py
```

### **View live logs:**
```bash
tail -f bot.log
```

### **View last 50 lines:**
```bash
tail -50 bot.log
```

### **Search for errors:**
```bash
grep -i error bot.log
```

---

## 🔄 Update Bot Later

When you make changes:

```bash
cd ~/solarkh_bot_new
git pull origin main
pkill -f bot.py
sleep 5
nohup python3.10 bot.py > bot.log 2>&1 &
```

---

## ✅ Success Checklist

- [ ] Logged into PythonAnywhere
- [ ] Opened Bash console
- [ ] Stopped old bot
- [ ] Pulled latest code
- [ ] Verified new files exist
- [ ] Started bot with nohup
- [ ] Checked bot.log for success message
- [ ] Tested `/start` in Telegram
- [ ] Tested `/products` command
- [ ] Tested `/learn` command
- [ ] Tested language switch
- [ ] Verified logo displays

---

## 🎉 You're Done!

Your bot is now running with:
- ✅ Product catalog
- ✅ Solar education
- ✅ Logo branding
- ✅ Bilingual support
- ✅ All features working

**Bot:** @solarkh_bot
**Channel:** @solar_kh
**Repo:** https://github.com/chhany007/solarkh_bot_new

---

## 📞 Quick Commands Reference

```bash
# Stop bot
pkill -f bot.py

# Start bot
nohup python3.10 bot.py > bot.log 2>&1 &

# Check status
ps aux | grep bot.py

# View logs
tail -f bot.log

# Update code
cd ~/solarkh_bot_new && git pull

# Restart bot
pkill -f bot.py && sleep 5 && nohup python3.10 bot.py > bot.log 2>&1 &
```

---

**Ready to deploy? Follow the steps above!** 🚀
