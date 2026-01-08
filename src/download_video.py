import yt_dlp
import os

YOUTUBE_URL = "https://youtu.be/mAFv55o47ok?si=wE6_CiD0NvcY0K1L"

VIDEO_DIR = "video"

os.makedirs(VIDEO_DIR, exist_ok=True)

ydl_opts = {
    "format": "best",
    "outtmpl": f"{VIDEO_DIR}/source_video.%(ext)s",
}

def download_video():
    """Download full video from YouTube"""
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([YOUTUBE_URL])
    
    print("Video downloaded successfully")

if __name__ == '__main__':
    download_video()