import discord
import redis

class ControllerViews(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.redis = redis.StrictRedis()
        
    @discord.ui.button(label="HBO", style=discord.ButtonStyle.primary)
    async def hbo(self, interaction, button):
        await interaction.response.defer()
        self.redis.publish('channel_test', '{"path": "hbo"}')
        