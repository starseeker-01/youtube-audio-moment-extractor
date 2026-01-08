import json
import subprocess
import os

TRANSCRIPT_PATH = "transcripts/transcript.json"
VIDEO_PATH = "video/source_video.mp4"

BUFFER = 15          # seconds before speech
CLIP_DURATION = 60   # seconds per clip

CATEGORIES = {
    "question": [
        "what", "why", "how", "when", "where",
        "who", "which", "can you", "do you", "is it"
    ],
    "agreement": [
        "i agree", "yes exactly", "that's right",
        "correct", "absolutely"
    ],
    "disagreement": [
        "i disagree", "i don't agree",
        "that's wrong", "not correct",
        "i don't think so"
    ]
}

for category in CATEGORIES:
    os.makedirs(f"clips/{category}", exist_ok=True)

def extract_clip(start_time, category, index):
    clip_start = max(0, start_time - BUFFER)
    output = f"clips/{category}/{category}_{index}.mp4"

    command = [
        "ffmpeg",
        "-y",
        "-ss", str(clip_start),
        "-i", VIDEO_PATH,
        "-t", str(CLIP_DURATION),
        "-c:v", "libx264",
        "-c:a", "aac",
        output
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def extract_all_clips():
    """Extract categorized clips based on transcript"""
    with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
        segments = json.load(f)

    counters = {key: 1 for key in CATEGORIES}

    for seg in segments:
        text = seg["text"].lower()
        start = seg["start"]

        for category, keywords in CATEGORIES.items():
            if any(k in text for k in keywords):
                extract_clip(start, category, counters[category])
                counters[category] += 1
                break

    print(" All clips extracted successfully")

if __name__ == "__main__":
    extract_all_clips()
