import yt_dlp
import os 

YOUTUBE_URL = "https://youtu.be/mAFv55o47ok?si=wE6_CiD0NvcY0K1L"

AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{AUDIO_DIR}/extracted.%(ext)s',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }
    ],
}

def download_audio():
    """Download audio from YouTube and convert to WAV"""
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([YOUTUBE_URL])
    print("Audio downloaded successfully")

if __name__ == "__main__":
    download_audio()