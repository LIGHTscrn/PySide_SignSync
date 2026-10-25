import yt_dlp
from typing import Dict, Any

class YoutubeMetadataExtractor:
    """
    Extarcts high-level metadata
    """

    def __init__(self):
        self.ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'skip_download': True,
                'noplaylist': True,
        }

    def extract(self, url:str) -> Dict[str, Any]:
        
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

                if not info:
                    return {"success": False,
                            "error": "No Metadata returned from video source."
                            }

                return {
                        "success": True,
                        "video_id": info.get('id'),
                        "title": info.get('title', 'Unknown Title'),
                        "channel": info.get('channel') or info.get('uploader', 'Unknown Creator'),
                        "duration": info.get('duration', 0),
                        "view_count": info.get('view_count', 0),
                        "thumbnail": info.get('thumbnail'),
                        "error": None
                }
        except yt_dlp.utils.DownloadError as e:
            return {"success": False, "error": f"Failed to access video : {str(e)}"}

        except Exception as e:
            return {"success": False, "error": f"Unexpected error: {str(e)}"}

