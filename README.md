# 🧠 Omani Arabic Voice Therapist Bot (CBT-Based)

> An AI-powered voice-only mental health chatbot built for culturally sensitive cognitive behavioral therapy (CBT) in **Omani Arabic**.

> [🎥 **Demo Video**](https://www.veed.io/view/dcf8f543-6327-4fa6-8931-5a62db1634fe?source=editor&panel=share)


![Status](https://img.shields.io/badge/status-MVP%20Complete-brightgreen)
![Flask](https://img.shields.io/badge/backend-Flask-blue)
![Speech](https://img.shields.io/badge/Speech-Google%20Cloud%20STT%2FTTS-yellow)

---

## 🗂 Features

* 🎙️ **Voice input only**: Users speak directly with the bot.
* 🧠 **GPT-J/Neo local LLM**: Generates culturally adapted CBT responses.
* 🔊 **Voice output**: Bot replies in spoken Omani Arabic using Google Cloud Text-to-Speech.
* 🚨 **Emergency detection**: Sensitive to crisis language (e.g., "أفكر أنهي حياتي").
* 🌍 **Dialect-aware**: Adapted to **Omani Arabic** and Gulf speech styles.

---

## 🖥️ Demo UI

```html
🎙 Record     🎧 Listen
---------------------------
User speaks...
Bot responds with voice
```

### 🎙 Record Button

* Captures audio via browser mic.
* Sends `.wav` file to `/chat`.

### 🎧 Listen Button

* Plays back the MP3 voice response from the bot.
* Supports in-browser playback.

---

## 🧠 CBT Persona Prompt

```text
أنت معالج نفسي من سلطنة عمان تستخدم العلاج المعرفي السلوكي وتتكلم بلهجة عمانية.
```

This ensures responses are **empathetic**, **relatable**, and **culturally relevant**.

---

## 🧪 Example Conversation

```txt
🧍 User: احس بيدك ولا زهقت من كل شيء.
🤖 Bot: فهمت عليك، كثير يحسون نفس الشعور. وش تتوقع سبب هذا الضيق؟ 
```

---

## 🚨 Emergency Handling

If phrases like:

```
أفكر أنهي حياتي
أبغي أموت
```

are detected, the system will trigger an **immediate escalation** and show an **emergency response message**.

---

## 🧰 Tech Stack

| Component       | Stack                              |
| --------------- | ---------------------------------- |
| Backend         | Flask (Python)                     |
| STT / TTS       | Google Cloud Speech + TTS          |
| LLM             | GPT-J 6B or GPT-Neo 1.3B (local)   |
| Voice Recording | Web browser mic (JS/HTML5)         |
| Hosting         | Localhost (can be deployed to GCP) |

---

## 📁 Folder Structure

```
voice_therapist/
│
├── app.py                    # Main Flask app
├── static/                   # Output audio files (.mp3)
├── templates/index.html      # Frontend UI
├── speech_to_text.py
├── text_to_speech.py
├── gpt_model.py
├── emergency_handler.py
├── cultural_filter.py
├── requirements.txt
└── README.md
```

---

## 📦 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourname/voice-therapist.git
cd voice-therapist
```

### 2. Setup a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Google Cloud credentials

In PowerShell (Windows):

```bash
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your_creds.json"
```

For Linux/Mac:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your_creds.json"
```

### 5. Run the app

```bash
python app.py
```

---

## 🙏 Credits

* **GPT-J / GPT-Neo** by EleutherAI
* **Google Cloud Speech API**
* Developed for AI voice therapy experiments in **Gulf Arabic**

---

## 💡 License

MIT License – Use responsibly. This project is **not a replacement for clinical mental health services**.



