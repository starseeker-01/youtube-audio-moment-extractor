import whisper
import json
import os

AUDIO_PATH = "audio/extracted.wav"
TRANSCRIPT_DIR = "transcripts"

os.makedirs("transcripts", exist_ok=True)

def transcribe_audio():
    """Transcribe audio using Whisper and save transcript"""
    print("Loading Whisper model...")
    model = whisper.load_model("base")

    print("Transcribing audio...")
    result = model.transcribe(AUDIO_PATH)

    with open(f"{TRANSCRIPT_DIR}/transcript.json", "w", encoding="utf-8") as f:
        json.dump(result["segments"], f, indent=2, ensure_ascii=False)

    with open(f"{TRANSCRIPT_DIR}/transcript.txt", "w", encoding="utf-8") as f:
        for seg in result["segments"]:
            f.write(f"[{seg['start']:.2f}s - {seg['end']:.2f}s]: {seg['text']}\n")

    print("Transcription completed")

if __name__ == "__main__":
    transcribe_audio()