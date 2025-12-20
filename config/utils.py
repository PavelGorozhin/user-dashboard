# utils.py
import logging
import os
from datetime import datetime

def get_current_timestamp():
    """Returns the current timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def configure_logging(log_level, log_file):
    """Configures the logging module.

    Args:
        log_level (str): The log level to use. One of 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.
        log_file (str): The file to write log messages to.
    """
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def get_config_value(config, key, default=None):
    """Gets a configuration value.

    Args:
        config (dict): The configuration dictionary.
        key (str): The key to look up.
        default (any, optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        any: The configuration value for the given key, or the default value if not found.
    """
    return config.get(key, default)

def get_env_value(key, default=None):
    """Gets an environment variable value.

    Args:
        key (str): The key to look up.
        default (any, optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        any: The environment variable value for the given key, or the default value if not found.
    """
    return os.getenv(key, default)