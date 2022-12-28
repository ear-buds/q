# import discord
from discord.ext import commands

class GetqCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("GetqCog is cogging.")

    @commands.command()
    async def getq(self, ctx):
        embed = discord.Embed(title="Help commands", description="Shows various help commands")
        embed.add_field(name="Show this help", value = "`/getq`", inline = False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GetqCog(bot))