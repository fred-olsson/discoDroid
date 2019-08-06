#!/usr/bin/env python3
import logging
import json

log = logging.getLogger(__name__)

with open('config.json', mode='r') as f:
    CONFIG = json.load(f)

LOG_FILE = CONFIG['logging']['handlers']['file_handler']['filename'][1:]
LOG_DIR = '/' + LOG_FILE.split('/')[1]