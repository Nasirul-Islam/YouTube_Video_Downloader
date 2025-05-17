from pytubefix import Playlist

# 🔗 Replace this with your playlist URL
playlist_url = input("Enter Youtube Playlist URL: ")

# Create a Playlist object
playlist = Playlist(playlist_url)


# Force load all videos before slicing
videos = list(playlist.videos)
videos_to_download = videos[49:]  
# Start from 10th video (index 9)

print(f"Downloading: {playlist.title}")

# Loop through all videos in the playlist 
# for video in playlist.videos: 

# Loop through all videos in the sliced playlist (starting from 49th video)
for video in videos_to_download:
    print(f"Downloading: {video.title}")
    try:
        # Download the highest resolution stream
        video.streams.get_highest_resolution().download()
    except Exception as e:
        print(f"❌ Failed to download {video.title}: {e}")

print("✅ All Videos Download Complete.")
