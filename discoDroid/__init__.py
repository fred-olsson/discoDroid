#!/usr/bin/env python3
import os
import json
import logging
import logging.config

#  Setup logging
with open('config.json', 'r') as f:
    CONFIG = json.load(f)

LOG_FILE = CONFIG['logging']['handlers']['file_handler']['filename'][1:]
LOG_DIR = '/' + LOG_FILE.split('/')[1]

if not os.path.exists(os.getcwd() + LOG_DIR):
    os.mkdir(os.getcwd() + LOG_DIR)

if not os.path.isfile(os.getcwd() + LOG_FILE):
    with open(os.getcwd() + LOG_FILE, 'w+', encoding='utf-8') as f:
        f.close()

logging.config.dictConfig(CONFIG['logging'])

log = logging.getLogger(__name__)

log.info('Log config initialised.')