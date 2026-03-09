import discord
import asyncio

def setup(Bot):
    GUILD_ID = discord.Object(id=1468209555761532980)
    @Bot.tree.command(name="chat" , description="chat with the bot" , guild=GUILD_ID)
    async def chat(interaction: discord.Interaction):
        await interaction.response.send_message("You have 67 IQ")
        await interaction.followup.send("ok but lets chat like normal humans right now")

        def check(message):
            return message.author == interaction.user and message.channel == interaction.channel

        try:
            msg = await Bot.wait_for('message', check=check, timeout=10)
            await answers(interaction, msg)
        except asyncio.TimeoutError:
            await interaction.followup.send("you took too long to respond")

    async def answers(interaction: discord.Interaction, msg):
        if msg.content.lower() == "bruh":
            await interaction.followup.send("bruh moment detected 💀")
        else:
            await interaction.followup.send(f"You said: {msg.content}")