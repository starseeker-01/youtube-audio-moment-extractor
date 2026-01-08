from download_audio import download_audio
from download_video import download_video
from transcribe import transcribe_audio
from extract_clips import extract_all_clips

def main():
    print("Starting YouTube Audio & Video Processing Pipeline")

    # Step 1: Download audio
    download_audio()

    # Step 2: Download video
    download_video()

    # Step 3: Transcribe audio
    transcribe_audio()

    # Step 4: Extract clips
    extract_all_clips()

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()
