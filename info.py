import discord

GUILD_ID = discord.Object(id=1468209555761532980)


def setup(bot):
    @bot.tree.command(name="serverhelp", description="decribes what is the server about", guild=GUILD_ID)
    async def help_command(interaction: discord.Interaction):
        await interaction.response.send_message("This server is about steam games and the stem peogram")

    @bot.tree.command(name="stem", description="explains what is stem", guild=GUILD_ID)
    async def stem_command(interaction: discord.Interaction):
        await interaction.response.send_message("STEM is: Science , Technology , Engineering and Mathematics")

    @bot.tree.command(name="steam", description=" explains what is steam", guild=GUILD_ID)
    async def steam_command(interaction: discord.Interaction):
        await interaction.response.send_message("steam is a video game digital distribution service by valve corporation")

    @bot.tree.command(name="physics", description="explain what is physics", guild=GUILD_ID)
    async def physics(interaction: discord.Interaction):
        await interaction.response.send_message("physics is a subject in science that explains the basic phenomena of the universe. it contains laws, like the newton laws.")

    @bot.tree.command(name="biology", description="explains what is biology", guild=GUILD_ID)
    async def biology(interaction: discord.Interaction):
        await interaction.response.send_message("Biology is the scientific study of living organisms — how they're structured, how they function, how they grow, reproduce, and interact with each other and their environment.")

    @bot.tree.command(name="chemistry", description="explains what is chemistry", guild=GUILD_ID)
    async def chemistry(interaction: discord.Interaction):
        await interaction.response.send_message("Chemistry is the scientific study of matter — what it's made of, how it behaves, and how substances interact and transform through chemical reactions.")
