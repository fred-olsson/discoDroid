#!/usr/bin/env python3
import os
import logging
import logging.config
from discoDroid.constants import CONFIG, LOG_DIR, LOG_FILE

# Setup logging, files and directories 

if not os.path.exists(os.getcwd() + LOG_DIR):
    os.mkdir(os.getcwd() + LOG_DIR)

if not os.path.isfile(os.getcwd() + LOG_FILE):
    with open(os.getcwd() + LOG_FILE, 'w+', encoding='utf-8') as f:
        f.close()

logging.config.dictConfig(CONFIG['logging'])

log = logging.getLogger(__name__)

log.info('Log config initialised.')