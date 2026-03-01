import os
import json
import discord
from discord.ext import commands

import info
import games
import jokes
import xp as xp_commands

try:
    with open("xp.json", "r") as f:
        user_xp = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    user_xp = {}

try:
    with open("rank.json", "r") as f:
        user_rank = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    user_rank = {}
try:
    with open("rank_advance" , "r") as f:
        rank_advance = json.load(f)
except:
    rank_advance = {}


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
        "slut" ,"cunt" , "retard" , "retarded" ,"fag" , "faggot" , "nigger" , "nigga" , "tranny" , "cancer",
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
        "you are dumb" , "you are stupied",
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

        await self.process_commands(message)


intents = discord.Intents.default()
intents.message_content = True
Bot = Client(command_prefix='!', intents=intents)

GUILD_ID = discord.Object(id=1468209555761532980)

info.setup(Bot)
games.setup(Bot, user_xp , rank_advance , user_rank)
xp_commands.setup(Bot, user_xp, user_rank , rank_advance)
jokes.setup(Bot)

token = os.getenv("DISCORD_BOT_TOKEN")
Bot.run(token)
