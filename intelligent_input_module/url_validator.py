import re 
from typing import Dict, Any


#Occurs when copied from the url while playing a video
Standard_link = "https://www.youtube.com/watch?v=QwHN36rSA5g"

#Occurs when share button is clicked
Shortened_link = "https://youtu.be/CJ5LC7f0Zus?si=1KQs-Na4QuOdtiH_"

#Occurs when an embed link is copied
embedded_link ="<iframe width="560" height="315" src="https://www.youtube.com/embed/QwHN36rSA5g?si=1Ge0kzbJAiwR2ohD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>"

#Occurs when a shorts link is copied
shorts_link = "https://youtube.com/shorts/Xhp2vwKWQ_g?si=wdWdts6GUAHjIr42"


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

        vido_id = match.group(1)
        reuturn {
                "valid" : True,
                "video_id" : video_id,
                "normalized_url" : f"https://youtube.com/watch?v={video_id}",
                "error": None
        }
            


