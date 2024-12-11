import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7587827209:AAE3BiNXrxwoGgIdUGWKhRvuJFm9rNukB0o")
API_ID = int(os.environ.get("API_ID", "16795822"))
API_HASH = os.environ.get("API_HASH", "791cc620cf2344a0fbf20b258fa679d2")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002297329742"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "7718122660 561339410").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://ivanstanley143:<ivanstanley143>@cluster0.zi4xs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "broadcast")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
https://graph.org/file/5ec5f5f926e1c5a31aa40-3e945218d176d4034f.jpg
