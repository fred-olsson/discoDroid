#!/usr/bin/env python3
import json
import logging
import discord
from discord.ext import commands
from discoDroid.checker import is_master

# User handling cog
#TODO: Add remove user, add remove roles?

class Users(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.log = logging.getLogger(__name__)

    @commands.command()
    @commands.check(is_master)
    async def add_user(self, ctx, role, user_id):
        if role == 'devs':
            await ctx.send('Cannot add or remove devs yet...')
            self.log.info(f'{ctx.author} denied access to users.devs')
            return
        with open('users.json', 'r') as f:
            users = json.load(f)
        users[role].append(int(user_id))
        with open('users.json', 'w') as f:
            json.dump(users, f)
        await ctx.send(f'Added user to the {role} role')
        self.log.info(f'{ctx.author} Added user {user_id} to the {role} role')
    
def setup(bot):
    bot.add_cog(Users(bot))