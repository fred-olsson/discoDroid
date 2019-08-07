#!/usr/bin/env python3
import logging
import discord
from discord.ext import commands

# Bot status cog

class Status(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.log = logging.getLogger(__name__)

    @commands.Cog.listener()
    async def on_ready(self):
        self.log.info('discoDroid lives!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')
        self.log.info(f'Ponged {ctx.author}')

def setup(bot):
    bot.add_cog(Status(bot))