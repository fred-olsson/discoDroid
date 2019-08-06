#!/usr/bin/env python3
import os
import logging
import discord
from discord.ext import commands
from discoDroid.constants import CONFIG

# Load bot and cogs.

bot = commands.Bot(command_prefix=CONFIG['discord']['prefix'])
log = logging.getLogger(__name__)

for cog in os.listdir('./discoDroid/cogs'):
    if (cog.endswith('.py')) and not (cog == '__init__.py'):
        bot.load_extension(f'discoDroid.cogs.{cog[:-3]}')
        log.info(f'Loaded cog: {cog}')

@bot.command()
async def ping(ctx):
    log = logging.getLogger(__name__)
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
    log.info('Ponged!')

@bot.event
async def on_ready():    
    log.info('discoDroid lives!')

bot.run(CONFIG['discord']['token'])