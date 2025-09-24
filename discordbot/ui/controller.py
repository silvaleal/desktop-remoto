import discord
import redis
from action.organizer import _pathButtons

class ControllerViews(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.redis = redis.StrictRedis()
        
    async def callback(self, interaction, path):
        await interaction.response.defer()
        data = {"path":path}
        self.redis.publish('channel_test', str(data).replace('"', "'").replace("'", '"'))
        
    @discord.ui.button(label="HBO", style=discord.ButtonStyle.primary, row=0)
    async def hbo(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.callback(interaction, 'hbo')

    @discord.ui.button(label="YouTube", style=discord.ButtonStyle.primary, row=0)
    async def yt(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.callback(interaction, 'youtube')

    @discord.ui.button(label="Force URL", style=discord.ButtonStyle.success, row=0)
    async def furl(self, interaction: discord.Interaction, button: discord.ui.Button): 
        await interaction.response.send_modal(ControllerFoceUrl())

    # Linha 1: navegação
    @discord.ui.button(label="↑", style=discord.ButtonStyle.secondary, row=1)
    async def up(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.callback(interaction, 'up')

    @discord.ui.button(label="↓", style=discord.ButtonStyle.secondary, row=1)
    async def down(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.callback(interaction, 'down')

    @discord.ui.button(label="←", style=discord.ButtonStyle.secondary, row=1)
    async def left(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.callback(interaction, 'left')

    @discord.ui.button(label="→", style=discord.ButtonStyle.secondary, row=1)
    async def right(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.callback(interaction, 'right')

    # Linha 2: ações
    @discord.ui.button(label="OK", style=discord.ButtonStyle.primary, row=2)
    async def ok(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.callback(interaction, 'ok')

    @discord.ui.button(label="Back", style=discord.ButtonStyle.danger, row=2)
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.callback(interaction, 'back')
    
class ControllerFoceUrl(discord.ui.Modal, title="Force-URL"):
    def __init__(self):
        super().__init__(timeout=None)
        self.redis = redis.StrictRedis()
    url = discord.ui.TextInput(label="URL")
    
    async def on_submit(self, interaction):
        await interaction.response.defer()
        data = {"url":self.url.value}
        self.redis.publish('channel_test', str(data).replace('"', "'").replace("'", '"'))