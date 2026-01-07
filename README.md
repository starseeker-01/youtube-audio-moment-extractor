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
├── audio/           # Downloaded audio files
├── video/           # Downloaded video files
├── transcripts/     # Generated transcripts
├── clips/           # Extracted moments
├── download_audio.py
├── download_video.py
├── transcribe.py
└── extract_clips.py
```
## Usage
1. Update URL in download files
2. Run: python download_audio.py
3. Run: python download_video.py
4. Run: python transcribe.py
5. Run: Python extract_clips.py
