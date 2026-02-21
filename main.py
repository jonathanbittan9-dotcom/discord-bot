import os
from asyncio import wait_for
from email.mime import message
import random

import discord
from discord.ext import commands
from discord import Intents, app_commands


class Client(commands.Bot):
    async def on_ready(self):
        await self.tree.sync(guild=GUILD_ID)
        print(f'logged on as {self.user}!')

    

    async def on_message(self, message):
        if message.author == self.user:
            return
        
intents=discord.Intents.default()
intents.message_content=True
Bot=Client(command_prefix='!', intents=intents)

GUILD_ID=discord.Object(id=1468209555761532980)
        
            
@Bot.tree.command(name="serverhelp", description="decribes what is the server about", guild=GUILD_ID)
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message("This server is about steam games and the stem peogram")
@Bot.tree.command(name="game" , description="play a game with the bot", guild=GUILD_ID)
async def game_command(interaction: discord.Interaction):
    await interaction.response.send_message("guess a number between 1 and 10")
    def check(message):
        return message.author == interaction.user and message.channel == interaction.channel
        
    try:
         msg= await Bot.wait_for('message', check=check, timeout=10)
    except:
        await interaction.followup.send("you took too long to respond")
        return

    if msg.content==str(random.randint(1,10)):
         await interaction.followup.send("you guessed the number correctly")
    else:
         await interaction.followup.send("you guessed the number incorrectly")
@Bot.tree.command(name="stem" , description="explains what is stem", guild=GUILD_ID)
async def stem_command(interaction: discord.Interaction):
    await interaction.response.send_message("STEM is: Science , Technology , Engineering and Mathematics")

@Bot.tree.command(name="steam" , description= " explains what is steam", guild=GUILD_ID)
async def steam_command(interaction: discord.Interaction):
    await interaction.response.send_message("steam is a video game digital distribution service by valve corporation")
@Bot.tree.command(name="calculator" , description="use the calculator", guild=GUILD_ID)
async def calculator_command(interaction: discord.Interaction, num1: int, operator: str, num2: int):
    if operator == "+":
        await interaction.response.send_message(num1+num2)
    elif operator == "-":
        await interaction.response.send_message(num1-num2)
    elif operator == "*":
        await interaction.response.send_message(num1*num2)
    elif operator == "/":
        if num2==0:
            await interaction.response.send_message("you cant divide by 0")
        else:
            await interaction.response.send_message(num1/num2)

token = os.getenv("DISCORD_BOT_TOKEN")

Bot.run(token)

