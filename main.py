import discord
from discord.ext import commands

from aioconsole import aexec

import sys
import io

out, err = io.StringIO(), io.StringIO()
sys.stdout = out
sys.stderr = err

activity = discord.Activity(type=discord.ActivityType.listening, name="eval")
bot = commands.Bot(command_prefix=['!'], activity=activity)

@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.command(name="eval")
async def eval(ctx,  *,python_code):
    # """for info do 'sudo help invite'"""
    python_code = python_code.replace("```py", "")
    python_code = python_code.replace("```", "")
    out, err = io.StringIO(), io.StringIO()
    sys.stdout = out
    sys.stderr = err

    await aexec(python_code)
    results = out.getvalue()
    errors = err.getvalue()
    if len(errors) < 25:
        embed = discord.Embed(title="Result", description=f"```py\n{results}\n```")
    else:
        embed = discord.Embed(title="Result", description=f"```py\n{errors}\n```")
    await ctx.send(embed=embed)

token = "ODc5NjMyNDk1OTk2NDUyODc0.YSSjmQ.G5CfjCEMzFxbDq8BYjHnjNvM7"
bot.run(token + "kk")
