from google.cloud import speech_v1 as speech
import tempfile

def transcribe_audio(audio_file):
    try:
        client = speech.SpeechClient()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
            audio_file.save(temp.name)
            temp.seek(0)
            content = temp.read()

        # ✅ First create the RecognitionAudio object with content
        audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=24000,  # Adjust this to match your .wav file
            language_code="ar-X-Gulf",  # Arabic Gulf dialect
        )

        # ✅ Now use audio in the recognize call
        response = client.recognize(config=config, audio=audio)

        print("🗣️ Full Google STT Response:", response)

        if not response.results:
            print("❌ No transcription result.")
            return ""

        return response.results[0].alternatives[0].transcript

    except Exception as e:
        print(f"❌ Transcription error: {e}")
        return ""
