@tree.command(name = "myq", description = "My first application Command") 
async def first_command(interaction):
    await interaction.response.send_message("`myq` called!")

import discord
from discord.ext import commands

class EnqCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def enq(self, ctx):
        embed = discord.Embed(title="Help commands", description="Shows various help commands")
        embed.add_field(name="Show this help", value = "`/help`", inline = False)
        await ctx.send(embed=embed)