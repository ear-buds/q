# import discord
from discord.ext import commands

class DeqCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("DeqCog is cogging.")

    @commands.command()
    async def deq(self, ctx):
        embed = discord.Embed(title="Help commands", description="Shows various help commands")
        embed.add_field(name="Show this help", value = "`/deq`", inline = False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(DeqCog(bot))