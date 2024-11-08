import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int("24779895")
API_HASH = getenv("24ca02336ac39cb748e2946de19814e3")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("6327930809:aaewwqavmw_a0pxotkkm8c2bmbfaf3jlw6m")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://GOKU:MISSBHOPALI@goku.pzzsl8d.mongodb.net/?retryWrites=true&w=majority", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 9999))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int("-1002210286036")

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int("6581286400")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/damian-bots/AXmusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Shorekeeper_updates")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Anime_Group_India_Chat")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-AviaxMusic-08-14")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("BQFToMkAG0GjvbqfQeLUc91gqnNlB6CsKxl7TD6PAWzm4dExPuqc_FY-wBcK5cdwOhofQw-3v0V95JL2VaLUzfwWJCJU2JBmig489F1PFVpm-HVjGbauWlh2-BAVp9TOrUVxJjCT3KS6083ZYpUBBvmeXl_DSW3vcDOXQ6Gb4NIqOxacra_dPFOXUD-9tRzO-n-vG7hpCm2u_P0k6arZ_3ECcY-Buc0OvKJwhZKYh85U-djZOukpymwDdYpQkRnwaW9zGq3JrU23OjZXeuAir_6_7EkcIpiznmTh8eA44-hjUEZzPQ0mR8dZTKHba6tAruO-YaVyXIZ0Ue22pvSO02DcrUOlewAAAABiNGsPAA", None)
STRING2 = getenv("BQFToMkAG0GjvbqfQeLUc91gqnNlB6CsKxl7TD6PAWzm4dExPuqc_FY-wBcK5cdwOhofQw-3v0V95JL2VaLUzfwWJCJU2JBmig489F1PFVpm-HVjGbauWlh2-BAVp9TOrUVxJjCT3KS6083ZYpUBBvmeXl_DSW3vcDOXQ6Gb4NIqOxacra_dPFOXUD-9tRzO-n-vG7hpCm2u_P0k6arZ_3ECcY-Buc0OvKJwhZKYh85U-djZOukpymwDdYpQkRnwaW9zGq3JrU23OjZXeuAir_6_7EkcIpiznmTh8eA44-hjUEZzPQ0mR8dZTKHba6tAruO-YaVyXIZ0Ue22pvSO02DcrUOlewAAAABiNGsPAA", None)
STRING3 = getenv("BQFToMkAG0GjvbqfQeLUc91gqnNlB6CsKxl7TD6PAWzm4dExPuqc_FY-wBcK5cdwOhofQw-3v0V95JL2VaLUzfwWJCJU2JBmig489F1PFVpm-HVjGbauWlh2-BAVp9TOrUVxJjCT3KS6083ZYpUBBvmeXl_DSW3vcDOXQ6Gb4NIqOxacra_dPFOXUD-9tRzO-n-vG7hpCm2u_P0k6arZ_3ECcY-Buc0OvKJwhZKYh85U-djZOukpymwDdYpQkRnwaW9zGq3JrU23OjZXeuAir_6_7EkcIpiznmTh8eA44-hjUEZzPQ0mR8dZTKHba6tAruO-YaVyXIZ0Ue22pvSO02DcrUOlewAAAABiNGsPAA", None)
STRING4 = getenv("BQFToMkAG0GjvbqfQeLUc91gqnNlB6CsKxl7TD6PAWzm4dExPuqc_FY-wBcK5cdwOhofQw-3v0V95JL2VaLUzfwWJCJU2JBmig489F1PFVpm-HVjGbauWlh2-BAVp9TOrUVxJjCT3KS6083ZYpUBBvmeXl_DSW3vcDOXQ6Gb4NIqOxacra_dPFOXUD-9tRzO-n-vG7hpCm2u_P0k6arZ_3ECcY-Buc0OvKJwhZKYh85U-djZOukpymwDdYpQkRnwaW9zGq3JrU23OjZXeuAir_6_7EkcIpiznmTh8eA44-hjUEZzPQ0mR8dZTKHba6tAruO-YaVyXIZ0Ue22pvSO02DcrUOlewAAAABiNGsPAA", None)
STRING5 = getenv("BQFToMkAG0GjvbqfQeLUc91gqnNlB6CsKxl7TD6PAWzm4dExPuqc_FY-wBcK5cdwOhofQw-3v0V95JL2VaLUzfwWJCJU2JBmig489F1PFVpm-HVjGbauWlh2-BAVp9TOrUVxJjCT3KS6083ZYpUBBvmeXl_DSW3vcDOXQ6Gb4NIqOxacra_dPFOXUD-9tRzO-n-vG7hpCm2u_P0k6arZ_3ECcY-Buc0OvKJwhZKYh85U-djZOukpymwDdYpQkRnwaW9zGq3JrU23OjZXeuAir_6_7EkcIpiznmTh8eA44-hjUEZzPQ0mR8dZTKHba6tAruO-YaVyXIZ0Ue22pvSO02DcrUOlewAAAABiNGsPAA5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/AJT.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/AJA.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/AJT.jpg"
STATS_IMG_URL = "https://graph.org/file/82d994fa7a374a52b2af6-536fd78cad0dfb1bbb.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/AJT.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/AJT.jpg"
STREAM_IMG_URL = "https://envs.sh/AJT.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/AJT.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/AJT.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/AJT.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/AJT.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/AJT.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
