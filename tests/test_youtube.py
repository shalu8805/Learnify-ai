import sys
sys.path.append(".")

from modules.youtube_processor import extract_video_id, get_transcript

url = input("YouTube URL paste karo: ")
print("Video ID:", extract_video_id(url))

segments = get_transcript(url)
print("Total segments:", len(segments))
for s in segments[:5]:
    print(s)