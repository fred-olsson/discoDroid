#!/usr/bin/env python3
import os
from os.path import dirname, abspath
import json
import logging
import logging.config

CONFIG_PATH = dirname(dirname(abspath(__file__))) + '/config.json'

#  Set up logging
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

LOG_PATH = config['logging']['handlers']['file_handler']['filename']

if not os.path.isfile(LOG_PATH):
    with open(LOG_PATH, 'w+', encoding='utf-8') as f:
        f.close()

logging.config.dictConfig(config['logging'])

log = logging.getLogger(__name__)

log.info('Log config initialised.')