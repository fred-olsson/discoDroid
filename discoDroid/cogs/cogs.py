#!/usr/bin/env python3
import logging
import discord
from discord.ext import commands

# Cog handler

class Cogs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.log = logging.getLogger(__name__)

    @commands.command()
    async def load(self, ctx, extension):
        self.bot.load_extension(f'discoDroid.cogs.{extension}')
        await ctx.send(f'Loaded cog: {extension}')
        self.log.info(f'Loaded cog: {extension}')
    
    @commands.command()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'discoDroid.cogs.{extension}')
        await ctx.send(f'Unloaded cog: {extension}')
        self.log.info(f'Unloaded cog: {extension}')

    @commands.command()
    async def reload(self, ctx, extension):
        self.bot.unload_extension(f'discoDroid.cogs.{extension}')
        self.bot.load_extension(f'discoDroid.cogs.{extension}')
        await ctx.send(f'Reloaded cog: {extension}')
        self.log.info(f'Reloaded cog: {extension}')

def setup(bot):
    bot.add_cog(Cogs(bot))