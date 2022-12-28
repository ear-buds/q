# import discord
from discord.ext import commands

class RegisterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("RegisterCog is cogging.")

    @commands.command()
    async def register(self, ctx):
        embed = discord.Embed(title="Help commands", description="Shows various help commands")
        embed.add_field(name="Show this help", value = "`/register`", inline = False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(RegisterCog(bot))