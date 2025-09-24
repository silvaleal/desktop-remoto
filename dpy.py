import discord
from discord.ext import commands
from discordbot.ui.controller import ControllerViews

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def controle(ctx):
    await ctx.send("Controle!",view=ControllerViews())

bot.run("")
