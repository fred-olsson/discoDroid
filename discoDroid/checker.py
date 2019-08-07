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
            log.info(f'{ctx.author} verified as Dev.')
            return True
    log.info(f'{ctx.author} denied Dev access.')

def is_master(ctx):
    if is_dev(ctx):
        return True
    log = logging.getLogger(__name__)
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    for user in users['masters']:
        if ctx.author.id == user:
            log.info(f'{ctx.author} verified as Master.')
            return True
    log.info(f'{ctx.author} denied Master access.')

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
            log.info(f'{ctx.author} verified as Assistant.')
            return True
    log.info(f'{ctx.author} denied Assistant access.')