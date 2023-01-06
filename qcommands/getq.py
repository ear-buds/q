import logging
# Discord.py
import discord
from discord.ext import commands
from discord import app_commands 

class GetqCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("GetqCog is cogging.")

    @app_commands.command(description="Get my Q.")
    @app_commands.default_permissions(administrator=True)
    async def myq(self, interaction : discord.Interaction, echo : str) -> None:
        logging.info("Getq Command called.")
        await interaction.response.send_message(echo)
        return

async def setup(bot):
    await bot.add_cog(GetqCog(bot))