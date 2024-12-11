import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7587827209:AAE3BiNXrxwoGgIdUGWKhRvuJFm9rNukB0o")
API_ID = int(os.environ.get("API_ID", "16795822"))
API_HASH = os.environ.get("API_HASH", "791cc620cf2344a0fbf20b258fa679d2")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "7718122660 561339410").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://damon:damon@cluster0.dxbn6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
