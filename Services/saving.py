from datetime import datetime
import os
import platform
from pathlib import Path
import json

def get_cache_path() -> Path:
    system = platform.system()

    if system == "Windows":
        path = Path(os.getenv("LOCALAPPDATA")) / "MultiAgentDebate" / "cache"

    elif system == "Darwin":  # macOS
        path = Path.home() / "Library" / "Caches" / "MultiAgentDebate"

    elif system == "Linux":
        path = Path(os.getenv("XDG_CACHE_HOME", Path.home() / ".cache")) \
               / "MultiAgentDebate"

    else:
        raise OSError(f"Unsupported operating system: {system}")

    path.mkdir(parents=True, exist_ok=True)

    return path

CACHE_PATH = get_cache_path()

def get_cache_message(cache_id: int):
    try:
        file_path = CACHE_PATH / f"{cache_id}.json"

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Could not find a session cache with this id ->", cache_id)
        return None


def save_cache(message: str = None) -> int:
    """Returning the id for cache"""

    files = os.listdir(CACHE_PATH)

    ids = []

    for file in files:
        try:
            ids.append(int(file.removesuffix(".json")))
        except ValueError:
            continue

    new_id = max(ids, default=0) + 1

    file_path = get_cache_path() / f"{new_id}.json"

    data = {}

    if message:
        data = {
            "time": datetime.now().isoformat(),
            "response": message,
            "id": 1
        }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return new_id

def delete_cache(id: int) -> bool:
    """Returning status if success True else False"""

    file_path = CACHE_PATH / f"{id}.json"

    if not file_path.is_file():
        return False

    try:
        file_path.unlink()
        return True
    except OSError:
        return False


def add_message_to_cache(id: int, message: str):
    """Add a message to an existing cache."""

    file_path = CACHE_PATH / f"{id}.json"

    if not file_path.is_file():
        return False

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}

        messages = data.get("messages", [])

        message_id = max(
            (msg["id"] for msg in messages),
            default=0
        ) + 1

        messages.append({
            "id": message_id,
            "time": datetime.now().isoformat(),
            "response": message
        })

        data["messages"] = messages

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    except (OSError, KeyError, TypeError):
        return False