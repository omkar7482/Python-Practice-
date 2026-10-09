import yt_dlp
import os

def download_highest_quality():
    url = input("Enter YouTube URL: ").strip()
    
    ydl_opts = {
        'outtmpl': os.path.join(os.path.expanduser('~'), 'Downloads', '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"🎬 Downloading: {info['title']}")
            print(f"📺 Quality: {info.get('format_note', 'Highest available')}")
            
            ydl.download([url])
        print("✅ Download completed!")
    except Exception as e:
        print(f"❌ Error: {e}")

download_highest_quality()