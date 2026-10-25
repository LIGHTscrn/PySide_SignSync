import re 
from typing import Dict, Any

class YoutubeURLValidator:
    """
    Validates youtube url formats and extracts 11-character video_id
    """

    def __init__(self):

        self.youtube_regex = re.compile(
                r'^(?:https?:\/\/)?(?:www\.)?'
                r'(?:youtube\.com\/(?:watch\?v=|embed\/|v\/|shorts\/)|youtu\.be\/)'
                r'([a-zA-Z0-9_-]{11})'
                r'(?:[?&].*)?$'
        )

    def validate(self,url: str) -> Dict[str,Any]:
        """
        Validates the input string and returns a structured result dictionary
        """

        if not url or not url.strip():
            return {"valid": False, "error": "Url field cannot be empty."}

        clean_url = url.strip()
        match = self.youtube_regex.match(clean_url)

        if not match:
            return {
                "valid" : False,
                "error": "Invalid Youtube URL format. Please provide a standard, shorts or youtu.be link"
        }

        video_id = match.group(1)
        return {
                "valid" : True,
                "video_id" : video_id,
                "normalized_url" : f"https://youtube.com/watch?v={video_id}",
                "error": None
        }
            


