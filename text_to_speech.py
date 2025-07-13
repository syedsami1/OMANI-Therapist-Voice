from google.cloud import texttospeech
import uuid
import os

def synthesize_speech(text, output_dir="static"):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="ar-X-Gulf",
        name="ar-XA-Wavenet-B"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    filename = f"audio_{uuid.uuid4().hex}.mp3"
    output_path = os.path.join(output_dir, filename)
    with open(output_path, "wb") as out:
        out.write(response.audio_content)

    return f"/static/{filename}"
