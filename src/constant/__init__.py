import imp


import os
from datetime import datetime
from tkinter import CURRENT


# Config file path in config directory
ROOT_DIR = os.getcwd()
CONFIG_DIR_NAME = "config"
CONFIG_FILE_NAME = "config.yml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR_NAME,CONFIG_FILE_NAME)


# Time Stamp Constant
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


# Logger Constants
LOG_DIR_NAME = "logs"