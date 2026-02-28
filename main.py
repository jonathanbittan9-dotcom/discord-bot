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
    user_xp = {}


try:
    with open("rank.json", "r") as f:
        user_rank =json.load(f)
except FileNotFoundError:
    user_rank = {}




class Client(commands.Bot):
    async def on_ready(self):
        await self.tree.sync(guild=GUILD_ID)
        print(f'logged on as {self.user}!')
       

    

    async def on_message(self, message):
        if message.author == self.user:
            return
        msg_content = message.content.lower()
        warn_words = [
        "fuck", "shit", "damn", "bitch" ,"ass" , "hell" , "crap" , "bastard" , "piss" , "whore" ,
        "slut" ,"cunt" , "retard" , "retarded" ,"fag" , "faggot" , "nigger" , "nigga" , "tranny" , "cancer"
        "die" , "died",
        "chink" ,"spic" , "kike" , "wetback" , "discord.gg" , "http://" , "https://" , "www." ,"bit.ly",
        "tinyurl" , ".com" , ".net" , ".org" , "kys" , "kill yourself" , "neck yourself" , "loser" , "idiot" ,
        "moron" , "stupid" , "dumb" , "ugly" , "fat" , "worthless" ,"pathetic" , "porn" , "sex" , "nude" , "naked",
        "nsfw" , "xxx" , "pornhub" , "xvideos" , "redtube" , "youporn" , "brazzers" , "bangbros" , "evilangel" , "digitalplayground",
        "explicit" , "@everyone" , "@here" , "black monkey"
        ]

        instant_ban_words = [
        "nigger" , "nigga" , "chink" , "spic" , "kike" , "wetback", "black monkey", "nazi",
        "i will kill you" , "i am going to kill you" , "gonna kill you" , "your address is" , "your phone number is",
        "i know where you live" , "i am coming for you" , "you better watch out" , "i will find you" , 
        "child porn" , "cp" , "loli" , "shota" , "rape" , "sexual assualt" , "kill yourself" , 
        "kys" , "hang yourself" , "neck yourself" , "commit suidice" , "drugs" , "i want drugs", 
        "make drugs" , "alcohol" , "make alcohol", "drunk" , "your real name is" , "you live at" , "your parents are",
        "you are dumb" , "you are stupied"
        "dumb" ,
        "ugly" ,
        "stupid" ,
        "you ip address is" , "you email address is" , 
        ]

        # if any(bad_word in msg_content for bad_word in warn_words):
        #     await message.delete()
        #     await message.channel.send(f"{message.author.mention} , you got a warn! its warn number {Warning_user[message.author.id]}! if you will get to 5 warns, you will be ban from the server!")
        #     Warning_user[message.author.id] += 1
        #     with open("warnings.json" , "w") as f:
        #         json.dump(Warning_user, f)
        #     if Warning_user == 5:
        #     #remember to generate the ban here

        
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
    user_id = str(interaction.user.id)
    if user_id not in user_xp:
        user_xp[user_id] = 0

    if msg.content=="dice":
        await interaction.followup.send(f'alright! , you will roll to dives, and if the numbers are the same you will get xp!')
        dice1= random.randint(1,6)
        dice2= random.randint(1,6)
        if dice1 == 1 and dice2 ==1:
            await interaction.followup.send(f'you rolled a double 1! you earned 10 xp!')
            user_xp[user_id] += 10
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        elif dice1 == 2 and dice2 == 2:
            await interaction.followup.send(f'you rolled a double 2! you earned 20 xp!')
            user_xp[user_id] += 20
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        elif dice1 == 3 and dice2 == 3:
            await interaction.followup.send(f'you rolled a double 3! you earned 30 xp!')
            user_xp[user_id] += 30
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        elif dice1 == 4 and dice2 == 4:
            await interaction.followup.send(f'you rolled a double 4! you earned 40 xp!')
            user_xp[user_id] += 40
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        elif dice1 == 5 and dice2 == 5:
            await interaction.followup.send(f'you rolled a double 5! you earned 50 xp!')
            user_xp[user_id] += 50
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        elif dice1 == 6 and dice2 == 6:
            await interaction.followup.send(f'you rolled a double 6! you earned 60 xp!')
            user_xp[user_id] += 60
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        else:
            await interaction.followup.send(f'you rolled a {dice1} and a {dice2} , you didnt earn any xp!')

    elif msg.content=="coin":
        gamble= random.choice(["heads","tails"])
        await interaction.followup.send(f'you flipped up a coin and got:{gamble}')
        if gamble == "heads":
            await interaction.followup.send("you earned 40 xp!")
            user_xp[user_id] += 40
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        elif gamble == "tails":
            if user_xp[user_id]<=0 or user_xp[user_id]<20:
                user_xp[user_id] = 0
                await interaction.followup.send("you cant lose any xp!")
            else:
                await interaction.followup.send("you lost 20 xp!")
                user_xp[user_id] -= 20
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')

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
            if user_xp[user_id]<=0 or user_xp[user_id]<50:
                user_xp[user_id] = 0
                await interaction.followup.send("you cant lose any xp!")
            else:
                user_xp[user_id] -= 50
                await interaction.followup.send("you lost 50 xp!")
            
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        elif number == 1000:
            await interaction.followup.send("you recieved the max number!")
            await interaction.followup.send("you earned 200 xp!")
            user_xp[user_id] += 200
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        elif number == 1:
            await interaction.followup.send("you recieved the min number!")
            if user_xp[user_id]<0 or user_xp[user_id]<20:
                user_xp[user_id]=0
                await interaction.followup.send("you cant lose any xp!")
            else:
                user_xp[user_id] -= 20
                await interaction.followup.send("you lost 20 xp!")
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        elif number == 500:
            await interaction.followup.send("you recieved the middle number!")
            await interaction.followup.send("you earned 20 xp!")
            user_xp[user_id] += 20
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
        elif number == 250:
            await interaction.followup.send("you recieved the quarter number!")
            await interaction.followup.send("you earned 10 xp!")
            user_xp[user_id] += 10
            with open("xp.json", "w") as f:
                json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
        else:
            await interaction.followup.send("you didnt recive any special number, you didnt earn or lose any xp!")
@Bot.tree.command(name="xp" , description="check your xp", guild=GUILD_ID)
async def xp_command(interaction: discord.Interaction):
    user_id = str(interaction.user.id)
    if user_id not in user_xp:
        user_xp[user_id] = 0
    await interaction.response.send_message(f'you have {user_xp[user_id]} xp')
@Bot.tree.command(name="shop" , description="check the shop: you can buy things with xp!", guild=GUILD_ID)
async def shop(interaction: discord.Interaction):
   await interaction.response.send_message("welcome to the shop! you can buy: role ")
@Bot.tree.command(name="physics" , description="explain what is physics", guild=GUILD_ID)
async def physics(interaction: discord.Interaction):
    await interaction.response.send_message("physics is a subject in science that explains the basic phenomena of the universe. it contains laws, like the newton laws.")
@Bot.tree.command(name="biology" , description="explains what is biology", guild=GUILD_ID)
async def biology(interaction:discord.Interaction):
    await interaction.response.send_message("Biology is the scientific study of living organisms — how they're structured, how they function, how they grow, reproduce, and interact with each other and their environment.")
@Bot.tree.command(name="chemistry" , description="explains what is chemistry", guild=GUILD_ID)
async def chemistry(interaction: discord.Interaction):
    await interaction.response.send_message("Chemistry is the scientific study of matter — what it's made of, how it behaves, and how substances interact and transform through chemical reactions.")
@Bot.tree .command(name="rank" , description="says your rank" , guild=GUILD_ID)
async def rank(interaction:discord.Interaction):

    await interaction.response.send_message(f"your rank is: {user_rank}")


token = os.getenv("DISCORD_BOT_TOKEN")

Bot.run(token)
