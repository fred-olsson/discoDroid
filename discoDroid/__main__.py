#!/usr/bin/env python3
import os
from os.path import dirname, abspath
import json
import logging
import discord
from discord.ext import commands

#TODO: TEST if can reach config file directly kthx.

CONFIG_PATH = dirname(dirname(abspath(__file__))) + '/config.json'

with open(CONFIG_PATH, mode='r') as f:
    config = json.load(f) 
bot = commands.Bot(command_prefix=config['discord']['prefix'])

@bot.event
async def on_ready():
    log = logging.getLogger(__name__)
    log.info('discoDroid lives!')

@bot.command()
async def ping(ctx):
    log = logging.getLogger(__name__)
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
    log.info('Ponged!')

bot.run(config['discord']['token'])