from ..settings import IniSettings, Url, IP, LogLevel
from pathlib import Path
from typing import Any

CONFIG_FILE: Path = Path("config.ini")
"""
Below required and optional data for running this software defined as a global scope
constant.
This constant is passed to the `settings` class; more info on the settings.py file.
"""
SETTINGS: dict[str, dict[str, object | dict[str, Any]]] = {
    "TELEGRAM": {
        "CHAT_ID": {"data": None, "typeOf": list, "required": False},
        "API_KEY": {"data": None, "typeOf": str, "required": True},
    },
    "SHINOBI": {
        "API_KEY": {"data": None, "typeOf": str, "required": True},
        "GROUP_KEY": {"data": None, "typeOf": str, "required": True},
        "BASE_URL": {"data": None, "typeOf": Url, "required": True},
        "PORT": {"data": 8080, "typeOf": int, "required": True},
    },
    "SHINOGRAMMA": {
        "LOGLEVEL": {"data": "info", "typeOf": LogLevel, "required": False},
        "PERSISTENCE": {"data": False, "typeOf": bool, "required": False},
        "BANS": {"data": None, "typeOf": dict, "required": False},
    },
    # "WEBHOOK": {"INCLUDE": WebhookServer},
}


if __name__ == "__main__":
    mySettings = IniSettings(neededSettings=SETTINGS, configFile=CONFIG_FILE)
    if not mySettings.iniRead():
        print("Error building and/or retrieving settings from config file, exiting...")
        raise SystemExit
