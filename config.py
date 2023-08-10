import re, os
import logging

id_pattern = re.compile(r'^.\d+$')
    
    API_ID = os.environ.get("API_ID", "")

    API_HASH = os.environ.get("API_HASH", "")

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 

    CAPTION = os.environ.get("CAPTION", "")

    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)

    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")

    OWNER_ID = os.environ.get("OWNER_ID", "")

    LIMIT = os.environ.get("LIMIT", "2500000")

    SKIP_NO = os.environ.get("SKIP_NO", "0")

    SESSION = os.environ.get("SESSION")

    TO_CHANNEL = os.environ.get("TO_CHANNEL", "")

    PORT = os.environ.get("PORT", "8080")

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
