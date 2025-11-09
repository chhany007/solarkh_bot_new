# 🚀 Deploy SolarKH Bot to PythonAnywhere (100% FREE)

## ✅ Why PythonAnywhere?
- **100% FREE** - No credit card required
- **Always-on** - Can run 24/7 with scheduled tasks
- **Easy setup** - No complex configuration
- **Web-based** - Everything in browser

---

## 📋 Step-by-Step Deployment

### **Step 1: Create PythonAnywhere Account**

1. Go to **https://www.pythonanywhere.com**
2. Click **"Pricing & signup"**
3. Choose **"Create a Beginner account"** (FREE)
4. Sign up with email
5. Verify email and login

---

### **Step 2: Upload Your Bot**

#### **Option A: From GitHub (Recommended)**

1. In PythonAnywhere, click **"Consoles"** tab
2. Click **"Bash"** to open terminal
3. Run these commands:

```bash
git clone https://github.com/chhany007/solarkh_bot.git
cd solarkh_bot
```

#### **Option B: Manual Upload**

1. Click **"Files"** tab
2. Create folder: `solarkh_bot`
3. Upload all files from your computer

---

### **Step 3: Install Dependencies**

In the **Bash console**:

```bash
cd solarkh_bot
pip3.10 install --user python-telegram-bot==20.4
```

Wait for installation (~1 minute)

---

### **Step 4: Test the Bot**

```bash
python3.10 bot.py
```

You should see:
```
✅ SolarKH Bot started successfully!
```

Press **Ctrl+C** to stop (we'll set up auto-run next)

---

### **Step 5: Create Always-On Script**

1. Click **"Files"** tab
2. Navigate to `solarkh_bot` folder
3. Create new file: `run_bot.sh`
4. Add this content:

```bash
#!/bin/bash
cd /home/YOUR_USERNAME/solarkh_bot
python3.10 bot.py
```

Replace `YOUR_USERNAME` with your PythonAnywhere username

5. Make it executable in Bash console:

```bash
chmod +x run_bot.sh
```

---

### **Step 6: Set Up Scheduled Task**

1. Click **"Tasks"** tab
2. Scroll to **"Scheduled tasks"**
3. Add new task:
   - **Time**: `00:00` (midnight)
   - **Command**: `/home/YOUR_USERNAME/solarkh_bot/run_bot.sh`
4. Click **"Create"**

**Note**: Free accounts can only run scheduled tasks once per day. For 24/7, see Step 7.

---

### **Step 7: Keep Bot Running 24/7 (Free Method)**

#### **Option A: Use Always-On Console**

1. Go to **"Consoles"** tab
2. Click **"Bash"**
3. Run:

```bash
cd solarkh_bot
nohup python3.10 bot.py > bot.log 2>&1 &
```

This runs the bot in background. To check if running:

```bash
ps aux | grep bot.py
```

To stop:
```bash
pkill -f bot.py
```

#### **Option B: Create Keepalive Script**

Create `keepalive.sh`:

```bash
#!/bin/bash
while true; do
    cd /home/YOUR_USERNAME/solarkh_bot
    python3.10 bot.py
    echo "Bot stopped. Restarting in 5 seconds..."
    sleep 5
done
```

Run it:
```bash
nohup bash keepalive.sh > bot.log 2>&1 &
```

---

### **Step 8: Verify Bot is Working**

1. Open Telegram: **https://t.me/solarkh_bot**
2. Send: `/start`
3. Try: `/language` → Choose Khmer
4. Test: `/quote 300 0.15`

---

## 🔧 Managing Your Bot

### **View Logs**

```bash
cd solarkh_bot
tail -f bot.log
```

### **Restart Bot**

```bash
pkill -f bot.py
cd solarkh_bot
nohup python3.10 bot.py > bot.log 2>&1 &
```

### **Update Bot**

```bash
cd solarkh_bot
git pull origin main
pkill -f bot.py
nohup python3.10 bot.py > bot.log 2>&1 &
```

---

## ⚠️ Important Notes

### **Free Account Limitations**
- Console sessions timeout after inactivity
- Need to restart bot if console closes
- Can upgrade to $5/month for always-on tasks

### **Keeping Bot Alive**
The bot may stop if:
- Console times out (use `nohup` to prevent)
- Server maintenance (restart manually)
- Account inactive for 3 months

### **Best Practice**
Check bot daily and restart if needed:
```bash
ps aux | grep bot.py
```

If not running:
```bash
cd solarkh_bot
nohup python3.10 bot.py > bot.log 2>&1 &
```

---

## 🆘 Troubleshooting

### **Bot not responding?**
```bash
# Check if running
ps aux | grep bot.py

# Check logs
tail -50 bot.log

# Restart
pkill -f bot.py
cd solarkh_bot
nohup python3.10 bot.py > bot.log 2>&1 &
```

### **Import errors?**
```bash
pip3.10 install --user python-telegram-bot==20.4
```

### **409 Conflict?**
Stop all other instances (Render, Railway, local)

---

## 💰 Cost Comparison

| Platform | Free Tier | Always-On | Credit Card |
|----------|-----------|-----------|-------------|
| **PythonAnywhere** | ✅ Yes | Manual restart | ❌ No |
| Render | ✅ Yes | ✅ Yes | ❌ No |
| Railway | ✅ Yes | ✅ Yes | ✅ Required |

---

## 📞 Support

- **PythonAnywhere Help**: https://help.pythonanywhere.com
- **Your Bot**: @solarkh_bot
- **Your Channel**: @solar_kh

---

**Your bot will be running on PythonAnywhere! 🎉**
