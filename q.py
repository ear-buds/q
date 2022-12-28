#############
#############
##### Q #####
#############
#############
        ####
          ###

# For loading the secrets
import os, sys
from dotenv import load_dotenv
import inspect
# Discord libraries
import discord
from discord.ext import commands

# Import commands for q
from qcommands import help
from qcommands import myq
from qcommands import enq
from qcommands import deq
from qcommands import getq
from qcommands import register


# Load the secrets
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Start the bot
bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())

# Register cogs for commands
# await bot.add_cog(Help(bot))

# Signal that the bot has connected
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    # await bot.add_cog(help.HelpCog(bot))

# Start the bot!
bot.run(TOKEN)