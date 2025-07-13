from flask import Flask, request

print("✅ Flask app loaded")

app = Flask(__name__)

@app.route("/")
def hello():
    print("🌐 / hit")
    return "Test app is running."

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Retrieve the audio file from the request
        audio_file = request.files["audio"]
        
        # Check if a file was uploaded
        if audio_file:
            # You can either process the file here or save it
            # For example, saving the file locally:
            audio_file.save("uploaded_audio.wav")
            
            # If you need to process the file (e.g., convert or analyze), 
            # you can use libraries like `pydub`, `wave`, or any other tool.

            # Respond back with a success message (or further processing result)
            return "Audio file received and processed!", 200
        else:
            return "No audio file found in the request.", 400
    except Exception as e:
        print(f"❌ Error: {e}")
        return "There was an error processing your request.", 500

if __name__ == "__main__":
    print("🚀 Running test server...")
    app.run(debug=True)
