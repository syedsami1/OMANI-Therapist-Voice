# 🚨 Emergency Detection & Safety Protocols

## 🛡️ Goal
To ensure the chatbot **detects mental health emergencies** and **safely escalates** when necessary.

---

## 🚨 Emergency Keyword Detection

When the transcript contains:
- **Self-harm phrases** (e.g., "أفكر أنهي حياتي", "ما في فائدة من الحياة")
- **Danger signals** (e.g., "تعبت من كل شيء", "أبغي أموت")

The system:

1. **Stops normal response flow.**
2. **Returns an emergency message**:
   > 🚨 تم التعرف على حالة طارئة. سيتم التواصل مع الجهات المختصة حالاً.
3. (Optional) **Triggers webhook or email notification** to a human moderator or local support line.

---

## 🧪 Sample Detection Snippet (Python)

```python
def check_emergency(transcript):
    keywords = [
        "أفكر أنهي حياتي",
        "أبغي أموت",
        "تعبت من كل شيء",
        "ما لي داعي"
    ]
    return any(phrase in transcript for phrase in keywords)
