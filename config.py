import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5164282725:AAFLnIpTYJGd_M-KGbpbkse2d4GKH0hU7u4")
API_ID = int(os.environ.get("API_ID", "1295756"))
API_HASH = os.environ.get("API_HASH", "1f2e07b7c28c4c734775879b23dff923")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002297329742"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "7718122660 561339410").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://ivanstanley143:<ivanstanley143>@cluster0.zi4xs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "broadcast")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
