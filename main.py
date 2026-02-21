import os
from asyncio import wait_for
import random
import json
import discord
from discord.ext import commands
from discord import Intents, Interaction, app_commands
try:
    with open("xp.json", "r") as f:
        user_xp = json.load(f)
except FileNotFoundError:
    user_id = str(interaction.user.id)
    if user_id not in user_xp:
        user_xp[user_id] = 0



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
@Bot.tree.command(name="gamble" , description="gamble and earn suprises!", guild=GUILD_ID)
async def gamble_command(interaction: discord.Interaction):
   
    await interaction.response.send_message("With what do you want to gamble? choose from: dice, coin, number")
    def check(message):
        return message.author == interaction.user and message.channel == interaction.channel
    try:
        msg= await Bot.wait_for('message' , check=check, timeout=10)
    except:
        await interaction.followup.send("you took too long to respond")
        return
    user_id = interaction.user.id
    if user_id not in user_xp:
        user_xp[user_id] = 0

    if msg.content=="dice":
        await interaction.followup.send(f'you rolled a dice and got: {random.randint(1,6)}')
    elif msg.content=="coin":
        await interaction.followup.send(f'you flipped up a coin and got:{random.choice(["heads","tails"])}')
    elif msg.content == "number":
        number= random.randint(1,1000)
        await interaction.followup.send(f'you recived the number:{number}')
        if number == 666:
            await interaction.followup.send("you recived the devil number!")
            await interaction.followup.send("by the way, you earned 30 xp!")
            user_xp[user_id] += 30
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
        elif number == 667:
            await interaction.followup.send("you recieved 67777777!!!!!!!")
            await interaction.followup.send("you earned 100 xp!")
            user_xp[user_id] += 100
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        elif number == 67:
            await interaction.followup.send("you recieved the regular 6777777!!!!!!!!!!")
            await interaction.followup.send("you earned 120 xp!")
            user_xp[user_id] += 120
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        elif number == 777:
            await interaction.followup.send("you recieved the lucky number!")
            await interaction.followup.send("you earned 50 xp!")
            user_xp[user_id] += 50
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        elif number == 900:
            await interaction.followup.send("you recieved the unlucky number!")
            await interaction.followup.send("you lost 50 xp!")
            user_xp[user_id] -= 50
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
       
    
    


token = os.getenv("DISCORD_BOT_TOKEN")

Bot.run(token)

