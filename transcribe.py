import whisper
import json
import os

# Load Whisper model
model = whisper.load_model("base")

# Transcribe audio
result = model.transcribe("audio/extracted.wav")

# Create transcripts folder
os.makedirs("transcripts", exist_ok=True)

# Save transcription as JSON
with open("transcripts/transcript.json", "w", encoding="utf-8") as f:
    json.dump(result["segments"], f, ensure_ascii=False, indent=2)

# Also save as text file
with open("transcripts/transcript.txt", "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        f.write(f"[{segment['start']:.2f}s - {segment['end']:.2f}s]: {segment['text']}\n")

print("Transcription completed. Files saved in transcripts/ folder")