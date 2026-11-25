import re
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    """YouTube URL se 11-character video ID nikalta hai."""
    patterns = [
        r"(?:v=)([A-Za-z0-9_-]{11})",
        r"youtu\.be/([A-Za-z0-9_-]{11})",
        r"youtube\.com/embed/([A-Za-z0-9_-]{11})",
    ]
    for p in patterns:
        match = re.search(p, url)
        if match:
            return match.group(1)
    return None


def get_transcript(url, languages=("en", "hi")):
    """
    URL leta hai, segments ki list deta hai:
    [{"start": 0.0, "end": 4.2, "text": "..."}, ...]
    Fail hone par ValueError uthata hai.
    """
    video_id = extract_video_id(url)
    if video_id is None:
        raise ValueError("Valid YouTube URL nahi hai.")

    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=list(languages))
    except Exception as e:
        raise ValueError(f"Captions nahi mile: {e}")

    segments = []
    for item in fetched:
        segments.append({
            "start": round(item.start, 2),
            "end": round(item.start + item.duration, 2),
            "text": item.text.replace("\n", " ").strip(),
        })
    return segments