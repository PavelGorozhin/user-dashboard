import logging
import json
from datetime import datetime

def configure_logger():
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s', 
        datefmt='%Y-%m-%d %H:%M:%S', 
        level=logging.INFO
    )

def load_config(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"Config file not found at {file_path}")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing config file: {e}")
        return None

def get_current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def validate_user_input(data):
    if not isinstance(data, dict):
        logging.error("Invalid input type. Expected a dictionary.")
        return False
    required_fields = ['username', 'email']
    for field in required_fields:
        if field not in data:
            logging.error(f"Missing required field: {field}")
            return False
    return True

class UtilsException(Exception):
    pass

def main():
    configure_logger()
    config = load_config('config.json')
    if config:
        logging.info("Config loaded successfully")
    else:
        logging.error("Failed to load config")

if __name__ == "__main__":
    main()