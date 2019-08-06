#!/usr/bin/env python3
import os
import json
import logging
import discord
from discord.ext import commands

with open('config.json', mode='r') as f:
    CONFIG = json.load(f) 

bot = commands.Bot(command_prefix=CONFIG['discord']['prefix'])

@bot.event
async def on_ready():
    log = logging.getLogger(__name__)
    log.info('discoDroid lives!')

@bot.command()
async def ping(ctx):
    log = logging.getLogger(__name__)
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
    log.info('Ponged!')

bot.run(CONFIG['discord']['token'])