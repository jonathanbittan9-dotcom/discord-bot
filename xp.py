import discord

GUILD_ID = discord.Object(id=1468209555761532980)


def setup(bot, user_xp, user_rank, rank_advance):
    @bot.tree.command(name="xp", description="check your xp", guild=GUILD_ID)
    async def xp_command(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if user_id not in user_xp:
            user_xp[user_id] = 0
        await interaction.response.send_message(f'you have {user_xp[user_id]} xp')

    @bot.tree.command(name="shop", description="check the shop: you can buy things with xp!", guild=GUILD_ID)
    async def shop(interaction: discord.Interaction):
        await interaction.response.send_message("welcome to the shop! you can buy: role ")

    @bot.tree.command(name="rank", description="says your rank", guild=GUILD_ID)
    async def rank(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        await interaction.response.send_message(f"your rank is: {user_rank.get(user_id, 0)}")
    