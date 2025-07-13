import os
from flask import Flask, request, jsonify, render_template
from speech_to_text import transcribe_audio
from gpt_model import generate_response
from text_to_speech import synthesize_speech
from cultural_filter import adapt_response
from emergency_handler import check_emergency

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\Dell\\Downloads\\voice-therapist-project-a7a2cc672204.json"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    audio_file = request.files["audio"]
    print("🎙️ /chat endpoint hit")
    print(f"📥 Received audio file: {audio_file.filename}")
    
    transcript = transcribe_audio(audio_file)
    print(f"📝 Transcript: {transcript}")

    if not transcript:
        return jsonify({"error": "Speech not recognized"}), 400

    if check_emergency(transcript):
        return jsonify({"response": "🚨 تم التعرف على حالة طارئة. سيتم التواصل مع الجهات المختصة حالاً."}), 200

    print("🧠 Loading GPT-J model...")
    raw_response = generate_response(transcript)
    print(f"💬 GPT Raw Response: {raw_response}")

    culturally_adapted = adapt_response(raw_response)
    print(f"💬 Culturally Adapted Response: {culturally_adapted}")

    output_audio_path = synthesize_speech(culturally_adapted)
    print(f"🎶 Audio Response Path: {output_audio_path}")

    return jsonify({
        "text": culturally_adapted,
        "audio_url": output_audio_path
    }), 200

if __name__ == "__main__":
    print("🚀 Launching app...")
    app.run(debug=True)
