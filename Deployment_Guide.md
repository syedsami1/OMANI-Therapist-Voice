# 🚀 Deployment Guide — Voice Therapist Bot

This guide walks you through running the Voice Therapist Bot locally or deploying it to a Google Cloud VM, ensuring secure, reliable access and full functionality.

---

## 💻 Local Development (Quick Setup)

### 1️⃣ Install Dependencies
```bash
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
```

### 2️⃣ Set Google Cloud Credentials
```bash
# Replace with your actual path to the key file
$env:GOOGLE_APPLICATION_CREDENTIALS = "C:/Users/Dell/Downloads/digital-elysium-428005-d6-36be7c917812.json"   # PowerShell
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"  # Bash/Mac/Linux
```

### 3️⃣ Run the Flask Bot
```bash
python app.py
```

---

## ☁️ Google Cloud VM Deployment

### 1️⃣ Create and Configure a VM
- OS: Ubuntu 20.04
- Specs: 2 vCPU+, 8GB RAM recommended
- Enable HTTP traffic during setup

### 2️⃣ Transfer Project Files to VM
```bash
gcloud compute scp --recurse voice_therapist your-vm-name:~/
```

### 3️⃣ SSH into VM and Set Up Bot
```bash
gcloud compute ssh your-vm-name

cd voice_therapist
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

export GOOGLE_APPLICATION_CREDENTIALS="~/credentials.json"
python app.py
```

---

## 🌐 Public Access Setup

Choose one of the options below to make the bot publicly accessible:

- **Ngrok**
  ```bash
  ngrok http 5000
  ```
  Share the generated URL for external access.

- **Custom Domain (Advanced)**
  - Install **nginx**
  - Configure reverse proxy to Flask
  - Add SSL via **Let's Encrypt**

---

## 📂 Sample Test Logs

These logs demonstrate how the bot handles different emotional cases.

### 🧠 Anxiety
```
User: شو أخبارك، أنا تعبان من التفكير الكثير  
Bot: أفهم شعورك، خلنا نهدأ شوي ونتنفس بعمق. إيش أكثر شيء يزعجك؟
```

### 👪 Family Stress
```
User: مشاكل في البيت، ما أقدر أتحمل  
Bot: البيت مرات يكون ضغط، بس دايم فيه حلول. تقدر تحكيلي أكثر؟
```

### 💼 Work Stress
```
User: أنا ما مرتاح في دوامي  
Bot: الشغل أحيانًا مرهق، خلنا نشوف كيف نخفف الضغط. ويش اللي مضايقك بالضبط؟
```

### 🚨 Crisis Response
```
User: ما في فايدة، أفكر أني أنهي حياتي  
Bot: 🚨 تم التعرف على حالة طارئة. سيتم التواصل مع الجهات المختصة حالاً.
```

### 🧬 Code-Switching Handling
```
User: I'm tired of this job wallah  
Bot: حاس فيك، الشغل لما يتعبنا نحاول نغير الروتين شوي. خلنا نحكي عن البدائل؟
```

---

## 📌 Notes
- Ensure your Google Cloud project has Speech-to-Text and Text-to-Speech APIs enabled.
- Bot relies on GPT-J locally; make sure model weights and dependencies are properly installed.
- Suicide detection triggers an escalation response; adapt integration responsibly.

