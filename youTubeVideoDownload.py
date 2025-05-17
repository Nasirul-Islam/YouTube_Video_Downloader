from pytubefix import YouTube, Playlist
import sys
# Run this command to build exe file 
# 1. pip install pyinstaller
# 2. pyinstaller --onefile .\youTubeVideoDownload.py 
def get_resolution_stream(video, quality):
    if quality == "high":
        return video.streams.filter(progressive=True, file_extension='mp4').order_by("resolution").desc().first()
    elif quality == "medium":
        return video.streams.filter(res="480p", progressive=True, file_extension='mp4').first() or \
               video.streams.filter(res="360p", progressive=True, file_extension='mp4').first()
    elif quality == "low":
        return video.streams.filter(progressive=True, file_extension='mp4').order_by("resolution").asc().first()
    return None

def download_videos(videos, quality):
    for i, video in enumerate(videos, start=1):
        try:
            print(f"▶️ [{i}/{len(videos)}] Downloading: {video.title}")
            stream = get_resolution_stream(video, quality)
            if stream:
                stream.download()
                print("✅ Done")
            else:
                print("⚠️ No stream found for the selected resolution.")
        except Exception as e:
            print(f"❌ Error downloading {video.title}: {e}")

def get_quality(): 
    # Quality Selection
    print("\nSelect resolution:")
    print("1. High (1080p/highest)")
    print("2. Medium (480p/360p)")
    print("3. Low (144p/lowest)")
    res_option = input("Choose quality (1/2/3): ").strip()
    
    quality_map = {"1": "high", "2": "medium", "3": "low"}
    quality = quality_map.get(res_option)
    if not quality:
        print("❌ Invalid resolution choice.")
        return None
    return quality


def main():
    print("Welcome To 📥 YouTube Downloader")
    print("Thanks To Using Nasirul's Apps.\n")
    while True : 
        print("1. Download single video")
        print("2. Download full playlist")
        print("3. Download partial playlist")
        print("4. Exit")
        option = input("Choose an option (1/2/3): ").strip()

        if option == "1":
            video_url = input("Enter the YouTube video URL: ").strip()
            try:
                video = YouTube(video_url)
                quality = get_quality()
                if quality==None: 
                    continue
                download_videos([video], quality)
                print("\n🎉 All done!\n")
            except: 
                print("Something went wrong,\nPlease give a valid URL")
        elif option == "2":
            playlist_url = input("Enter the YouTube playlist URL: ").strip()
            try:
                playlist = Playlist(playlist_url) 
                videos = list(playlist.videos)
                print(f"📺 Playlist: {playlist.title} | Total videos: {len(videos)}")
                quality = get_quality()
                if quality==None: 
                    continue
                download_videos(videos, quality)
                print("\n🎉 All done!\n")
            except: 
                print("Something went wrong,\nPlease give a valid URL")
            
        elif option == "3":
            playlist_url = input("Enter the YouTube playlist URL: ").strip()
            try:
                playlist = Playlist(playlist_url)
                videos = list(playlist.videos)
                print(f"📺 Playlist: {playlist.title} | Total videos: {len(videos)}")

                start = int(input("Enter start video number (e.g. 1): ")) - 1
                end = int(input("Enter end video number (e.g. 5): "))
                if start < 0 or end > len(videos) or start >= end:
                    print("❌ Invalid range.")
                    continue
                    # sys.exit()

                selected_videos = videos[start:end]
                quality = get_quality()
                if quality==None: 
                    continue
                download_videos(selected_videos, quality)
                print("\n🎉 All done!\n")
            except: 
                print("Something went wrong,\nPlease give a valid URL")
        elif option == "4": 
            print("Exit option selected.")
            sys.exit()
        else:
            print("\nPlease Choose a valid option.")
        
if __name__ == "__main__":
    main()
