import logging
# Discord.py
import discord
from discord.ext import commands
from discord import app_commands 

class MyqCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("MyqCog is cogging.")

    @commands.command()
    async def sync(self, ctx) -> None:
        cmds = await ctx.bot.tree.sync()
        self.bot.tree.copy_global_to(guild=ctx.guild)
        await ctx.send(f"{len(cmds)} commands are synced.")
        return

    @app_commands.command(description="Show my Q.")
    @app_commands.default_permissions(administrator=True)
    async def myq(self, interaction : discord.Interaction, echo : str) -> None:
        logging.info("Myq Command called.")
        await interaction.response.send_message(echo)
        return

async def setup(bot):
    await bot.add_cog(MyqCog(bot))