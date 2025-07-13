# 📊 Model Evaluation Report

## ✅ Model Used
- `EleutherAI/gpt-j-6B` via Hugging Face Transformers

## 🧪 Alternatives Considered
| Model         | Why Rejected                |
|---------------|-----------------------------|
| GPT-Neo       | Less coherent, less empathetic |
| DialoGPT      | Not suitable for Arabic / CBT |
| GPT-3.5 / 4   | Not usable (paid / not allowed) |

## 🔍 Why GPT-J?
- Open-source
- Works offline or locally
- Good generation control with prompt design
- Fine-tunable in future

## ⚙️ Prompt Design
- Custom prompt ensures CBT and Omani dialect
- Example: `"أنت معالج نفسي عماني..."`

## 🚀 Performance
- Runs ~12s per response on RTX 4090 or A100
