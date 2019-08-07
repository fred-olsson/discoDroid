#!/usr/bin/env python3
import logging
import json

# Permission checks.

def is_dev(ctx):
    log = logging.getLogger(__name__)   
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    for user in users['devs']:
        if ctx.author.id == user:
            log.info('Dev verified.')
            return True
    log.info('Dev denied.')

def is_master(ctx):
    if is_dev(ctx):
        return True
    log = logging.getLogger(__name__)
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    for user in users['masters']:
        if ctx.author.id == user:
            log.info('Master verified.')
            return True
    log.info('Master denied.')

def is_assistant(ctx):
    if is_dev(ctx):
         return True    
    if is_master(ctx):
         return True
    log = logging.getLogger(__name__)
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    for user in users['assistants']:
        if ctx.author.id == user:
            log.info('Assistant verified.')
            return True
    log.info('Assistant denied.')