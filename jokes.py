import discord

GUILD_ID = discord.Object(id=1468209555761532980)
def setup(bot):
    @bot.tree.command(name="rickroll", description="never gonna give you up", guild=GUILD_ID)
    async def rickroll(interaction: discord.Interaction):
        await interaction.response.send_message("https://media.tenor.com/x8v1oNUOmg4AAAAM/rickroll-roll.gif")

