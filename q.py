# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f'{client.user} has connected to Discord!')

@tree.command(name = "commandname", description = "My first application Command") 
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

client.run(TOKEN)
