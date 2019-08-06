#!/usr/bin/env python3
import logging
import json

log = logging.getLogger(__name__)

with open('config.json', 'r') as f:
    CONFIG = json.load(f)

LOG_FILE = CONFIG['logging']['handlers']['file_handler']['filename'][1:]
LOG_DIR = '/' + LOG_FILE.split('/')[1]

def is_dev(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
    for user in users['devs']:
        if ctx.author.id == user:
            return True