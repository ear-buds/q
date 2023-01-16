import logging
# Discord.py
import discord
from discord.ext import commands
from discord import app_commands 

class RegisterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("RegisterCog is cogging.")

    @app_commands.command(description="Register a user.")
    @app_commands.default_permissions(administrator=True)
    async def register(self, interaction : discord.Interaction, echo : str) -> None:
        logging.info("Register Command called.")
        await interaction.response.send_message(echo)
        return

async def setup(bot):
    await bot.add_cog(RegisterCog(bot))