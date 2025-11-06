import os
import json
import logging
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

logger = logging.getLogger(__name__)

def read_json_file(file_path: str) -> Dict[str, Any]:
    """Read and parse a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error reading JSON file {file_path}: {e}")
        raise

def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    """Write data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    except (IOError, TypeError) as e:
        logger.error(f"Error writing JSON file {file_path}: {e}")
        raise

def ensure_directory_exists(dir_path: str) -> None:
    """Ensure a directory exists; create it if not."""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        logger.info(f"Created directory: {dir_path}")

def get_timestamp_string() -> str:
    """Return a timestamp string in ISO format."""
    return datetime.utcnow().isoformat()

def filter_dict(data: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    """Filter a dictionary to include only specified keys."""
    return {k: v for k, v in data.items() if k in keys}

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries, with dict2 values taking precedence."""
    return {**dict1, **dict2}

def validate_config(config: Dict[str, Any], required_keys: List[str]) -> bool:
    """Validate that a config dictionary contains all required keys."""
    missing_keys = [key for key in required_keys if key not in config]
    if missing_keys:
        logger.error(f"Missing required config keys: {missing_keys}")
        return False
    return True

def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks of specified size."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]