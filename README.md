# YouTube Audio Moment Extractor

##  Project Description
AI-based system to extract key moments (Q&A, Agreement, Disagreement) from YouTube videos.

##  Week 1 Progress
-  YouTube audio/video download
-  Whisper transcription
-  Basic keyword-based moment detection
-  Clip extraction with buffer time

##  Installation
```bash
pip install -r requirements.txt
```
##  Project Structure
```
youtube_audio_moment_extractor/
├── audio/               # Downloaded audio files (.wav)
├── video/               # Downloaded video files (.mp4)
├── transcripts/         # Generated transcripts (.txt)
├── clips/               # Extracted video clips
│   ├── agreement/       # Clips with agreement moments
│   ├── disagreement/    # Clips with disagreement moments
│   └── question/        # Clips with Q&A moments
├── src/                 # Source code modules
│   ├── download_audio.py
│   ├── download_video.py
│   ├── transcribe.py
│   ├── extract_clips.py
│   └── main.py          # Pipeline controller (optional)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

```
## Usage
1. Update URL in download files
2. Run each module in sequence:
  - python src/download_audio.py
  - python src/download_video.py
  - python src/transcribe.py
  - python src/extract_clips.py
3. Optionally, run the full pipeline via:
  - python src/main.py

