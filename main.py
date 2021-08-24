import discord
from discord.ext import commands


activity = discord.Activity(type=discord.ActivityType.listening, name="eval")

bot = commands.Bot(command_prefix=['!'], intents=intents, activity=activity)

@bot.command(name="eval")
async def eval(ctx,  *,python_code):
    # """for info do 'sudo help invite'"""
    python_code = python_code.replace("```py", "")
    python_code = python_code.replace("```", "")
    embed = discord.Embed(title="Result", description=f"```py{eval(python_code)}\n```", color="#FFFFFF")
    await ctx.send(embed=embed)

token = "ODc5NjMyNDk1OTk2NDUyODc0.YSSjmQ.G5CfjCEMzFxbDq8BYjHnjNvM7"
bot.run(token + "kk")
