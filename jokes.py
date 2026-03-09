import discord

GUILD_ID = discord.Object(id=1468209555761532980)
def setup(bot):
    @bot.tree.command(name="rickroll", description="never gonna give you up", guild=GUILD_ID)
    async def rickroll(interaction: discord.Interaction):
        await interaction.response.send_message("https://media.tenor.com/x8v1oNUOmg4AAAAM/rickroll-roll.gif")
    @bot.tree.command(name="hate" , description="i hate you lol" , guild=GUILD_ID)
    async def hate(interaaction: discord.Interaction):
        await interaaction.response.send_message("https://tenor.com/view/i-hate-you-anakin-star-wars-gif-10358450")
    @bot.tree.command(name="lol" , description="lol" , guild=GUILD_ID)
    async def lol(interaction: discord.Interaction):
        await interaction.response.send_message("https://discord.com/channels/@me/1451235592145866999/1480236786734202981")
