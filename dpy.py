import discord
from discord.ext import commands
from discordbot.ui.controller import ControllerViews

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!",view=ControllerViews())

bot.run("MTM5MjEzNjY3MDAwNjA4MzY0NA.G80i0g.yWzzzSJoSXB2kITrWuQHDeabPaDNn2A6BXtiPc")
