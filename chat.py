import discord
import json
def setup(Bot):
    GUILD_ID = discord.Object(id=1468209555761532980)
    @Bot.tree.command(name="chat" , description="chat with the bot" , guild=GUILD_ID)
    async def chat(interaction: discord.Interaction):
        await interaction.response.send_message("You have 67 IQ")