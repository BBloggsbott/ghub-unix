import json
import os

from ghubunix.models.config import Config

CONFIG_DIR_NAME = ".ghubunix"
HOME_DIR = os.path.expanduser("~")
CONFIG_DIR = os.path.join(HOME_DIR, CONFIG_DIR_NAME)
CONFIG_FILE_NAME = "config.json"


def create_dir(dir: str):
    """Create a directory

    Args:
        dir(str): Directory name
    """
    if not os.path.isdir(dir):
        os.mkdir(dir)


def save_config(
    config: Config,
    config_dir: str = CONFIG_DIR,
    config_file_name: str = CONFIG_FILE_NAME,
):
    """Save the config

    Args:
        config(Config): Config object to save
        config_dir(str): Directory to save the config
        config_file_name: Name of the Config file
    """
    create_dir(config_dir)
    file_name = os.path.join(config_dir, config_file_name)
    with open(file_name, "w+") as config_file:
        json.dump(config.dict(), config_file, indent=4)


def load_config(config_dir: str = CONFIG_DIR, config_file_name: str = CONFIG_FILE_NAME):
    """Load config from config file

    Args:
        config_dir(str): Directory to save the config
        config_file_name: Name of the Config file
    """
    if os.path.isdir(config_dir):
        file_name = os.path.join(config_dir, config_file_name)
        with open(file_name, "r") as config_file:
            config_dict = json.load(config_file)
        config = Config(**config_dict)
        return config
