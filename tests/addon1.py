from ..settings import AddressKList
from typing import Any

class WebHookServer:
    """
    A dummy class to test INCLUDE functionality of settings module.
    """

    # Required settings for this class, you can use "INCLUDE" in settings module
    SETTINGS: dict[str, object | dict[str, Any]] = {
        "SERVER": {"data": False, "typeOf": bool, "required": False},
        "PORT": {"data": 5001, "typeOf": int, "required": False},
        "WEBHOOKS": {"data": None, "typeOf": AddressKList, "required": False},
        "REQUESTS_RATE_LIMIT": {"data": 10, "typeOf": float, "required": False},
        "IP": {"data": None, "typeOf": str, "required": True},
    }
