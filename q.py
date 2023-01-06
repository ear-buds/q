#############
#############
##### Q #####
#############
#############
        ####
          ###

##### For loading the secrets
import os, sys, asyncio
from dotenv import load_dotenv

##### Discord libraries
import discord
from discord.ext import commands

##### Set up logging
import logging
discord.utils.setup_logging()

##### Load all the commands
async def load_extensions(bot):
    for commandfile in os.listdir("qcommands"):
        if commandfile.endswith(".py") and not commandfile.startswith("_"):
            # Remove filetype
            commandfile = commandfile[:-3] # negative slice
            # Construct the dot name
            dot_name = f"qcommands.{commandfile}"
            await bot.load_extension(f"{dot_name}")

# Start the bot!
async def main(TOKEN):
    # Start the bot
    intents = discord.Intents.default()
    intents.message_content = True
    async with commands.Bot(command_prefix="/", intents=intents) as bot:
        # Signal that the bot has connected
        @bot.event
        async def on_ready():
            logging.info(f'{bot.user} has connected to Discord!')
        # Load Extensions
        await load_extensions(bot)
        # Start the event loop -- missing logging, though
        await bot.start(TOKEN)
        
# This is the "Main" function
## Essentially it just detects that the code is being executed from running
## this file, as opposed to running it from some other file
if __name__ == "__main__":
    # Load the secrets
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    # Start the bot
    asyncio.run(main(TOKEN))