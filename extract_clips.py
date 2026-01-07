import json
import subprocess
import os

TRANSCRIPT_PATH = "transcripts/transcript.json"
VIDEO_PATH = "video/source_video.mp4"

BUFFER = 15        # seconds before event
CLIP_DURATION = 60 # seconds total clip length

with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
    segments = json.load(f)

os.makedirs("clips/question_answer", exist_ok=True)
os.makedirs("clips/agreement", exist_ok=True)
os.makedirs("clips/disagreement", exist_ok=True)

question_words = [
    "what", "why", "how", "when", "where",
    "who", "which", "can you", "do you", "is it"
]

agreement_phrases = [
    "i agree",
    "yes exactly",
    "that's right",
    "correct",
    "absolutely"
]

disagreement_phrases = [
    "i disagree",
    "i don't agree",
    "that's wrong",
    "not correct",
    "i don't think so"
]

qa_idx = 1
agree_idx = 1
disagree_idx = 1

def extract_clip(start_time, category, index):
    clip_start = max(0, start_time - BUFFER)
    output_path = f"clips/{category}/{category}_{index}.mp4"

    cmd = [
        "ffmpeg",
        "-y",
        "-ss", str(clip_start),
        "-i", VIDEO_PATH,
        "-t", str(CLIP_DURATION),
        "-c:v", "libx264",
        "-c:a", "aac",
        output_path
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

for seg in segments:
    text = seg["text"].lower()
    start = seg["start"]

    if any(q in text for q in question_words):
        extract_clip(start, "question_answer", qa_idx)
        qa_idx += 1

    elif any(a in text for a in agreement_phrases):
        extract_clip(start, "agreement", agree_idx)
        agree_idx += 1
    
    elif any(d in text for d in disagreement_phrases):
        extract_clip(start, "disagreement", disagree_idx)
        disagree_idx +=1

print("Clip extraction completed with audio")