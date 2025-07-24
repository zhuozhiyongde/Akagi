import os
import json
import jsonschema
from jsonschema.exceptions import ValidationError
import dataclasses
from enum import Enum
from pathlib import Path
from .logger import logger

FILE_PATH = Path(__file__).resolve().parent


class MITMType(Enum):
    AMATSUKI = "amatsuki"
    MAJSOUL = "majsoul"
    RIICHI_CITY = "riichi_city"
    TENHOU = "tenhou"

@dataclasses.dataclass
class ServiceConfig:
    host: str
    port: int

@dataclasses.dataclass
class MITMConfig(ServiceConfig):
    type: MITMType

@dataclasses.dataclass
class Settings:
    mitm: MITMConfig
    frontend: ServiceConfig
    model: str
    auto_switch_model: bool
    def update(self, settings: dict) -> None:
        """
        Update settings from a dictionary

        Args:
            settings (dict): Dictionary with settings to update
        """
        self.mitm.host = settings["mitm"]["host"]
        self.mitm.port = settings["mitm"]["port"]
        self.mitm.type = MITMType(settings["mitm"]["type"])
        self.frontend.host = settings["frontend"]["host"]
        self.frontend.port = settings["frontend"]["port"]
        self.model = settings["model"]
        self.auto_switch_model = settings["auto_switch_model"]

    def save(self) -> None:
        """
        Save the settings to the settings.json file
        """
        with open(FILE_PATH / "settings.json", "w") as f:
            json.dump({
                "mitm": {
                    "type": self.mitm.type.value,
                    "host": self.mitm.host,
                    "port": self.mitm.port
                },
                "frontend": {
                    "host": self.frontend.host,
                    "port": self.frontend.port
                },
                "model": self.model,
                "auto_switch_model": self.auto_switch_model
            }, f, indent=4)
        # Save the settings to the file
        logger.info(f"Saved settings to {FILE_PATH / 'settings.json'}")
        logger.info(f"Updated {FILE_PATH / 'settings.json'} with new settings")

def load_settings() -> Settings:
    """
    Load settings from settings.json and validate them against settings.schema.json

    Raises:
        FileNotFoundError: settings.json or settings.schema.json not found
        jsonschema.exceptions.ValidationError: settings.json does not match settings.schema.json

    Returns:
        Settings: Parsed settings
    """

    # Check file exists
    if not (FILE_PATH / "settings.json").exists():
        raise FileNotFoundError("settings.json not found")
    if not (FILE_PATH / "settings.schema.json").exists():
        raise FileNotFoundError("settings.schema.json not found")
    
    try:
        # Load settings
        with open(FILE_PATH / "settings.json", "r") as f:
            settings = json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"settings.json corrupted: {e}")
        logger.warning("Backup settings.json to settings.json.bak")
        os.rename(FILE_PATH / "settings.json", FILE_PATH / "settings.json.bak")
        logger.warning("Creating new settings.json")
        with open(FILE_PATH / "settings.json", "w") as f:
            json.dump({
                "mitm": {
                    "type": "majsoul",
                    "host": "0.0.0.0",
                    "port": 7880
                },
                "model": "mortal",
                "auto_switch_model": True,
                "frontend": {
                    "host": "frontend-serve",
                    "port": 3001
                }
            }, f, indent=4)
        logger.info(f"Created new settings.json with default values")
        # Load settings again
        with open(FILE_PATH / "settings.json", "r") as f:
            settings = json.load(f)

    # Load schema
    with open(FILE_PATH / "settings.schema.json", "r") as f:
        schema = json.load(f)

    # Validate settings
    # This will raise an exception if the settings are invalid
    jsonschema.validate(settings, schema)

    # Parse settings
    return Settings(
        mitm=MITMConfig(
            host=settings["mitm"]["host"],
            port=settings["mitm"]["port"],
            type=MITMType(settings["mitm"]["type"])
        ),
        frontend=ServiceConfig(
            host=settings.get("frontend", {}).get("host", "localhost"),
            port=settings.get("frontend", {}).get("port", 3001)
        ),
        model=settings["model"],
        auto_switch_model=settings["auto_switch_model"]
    )

def get_schema() -> dict:
    """
    Get the schema for settings.json

    Returns:
        dict: Schema for settings.json
    """
    with open(FILE_PATH / "settings.schema.json", "r") as f:
        return json.load(f)
    
def get_settings() -> dict:
    """
    Get the settings.json

    Returns:
        dict: settings.json
    """
    with open(FILE_PATH / "settings.json", "r") as f:
        return json.load(f)
    
def save_settings(settings: dict) -> None:
    """
    Save the settings.json

    Args:
        settings (dict): settings.json
    """
    with open(FILE_PATH / "settings.json", "w") as f:
        json.dump(settings, f, indent=4)

def verify_settings(settings: dict) -> bool:
    """
    Verify the settings.json against the schema

    Args:
        settings (dict): settings.json

    Returns:
        bool: True if valid, False otherwise
    """
    try:
        jsonschema.validate(settings, get_schema())
        return True
    except ValidationError as e:
        logger.error(f"Settings validation error: {e.message}")
        return False

settings: Settings = load_settings()