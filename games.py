import discord
import random
import json

GUILD_ID = discord.Object(id=1468209555761532980)


def setup(bot, user_xp):
    @bot.tree.command(name="game", description="play a game with the bot", guild=GUILD_ID)
    async def game_command(interaction: discord.Interaction):
        await interaction.response.send_message("guess a number between 1 and 10")

        def check(message):
            return message.author == interaction.user and message.channel == interaction.channel

        try:
            msg = await bot.wait_for('message', check=check, timeout=10)
        except:
            await interaction.followup.send("you took too long to respond")
            return

        if msg.content == str(random.randint(1, 10)):
            await interaction.followup.send("you guessed the number correctly")
        else:
            await interaction.followup.send("you guessed the number incorrectly")

    @bot.tree.command(name="gamble", description="gamble and earn suprises!", guild=GUILD_ID)
    async def gamble_command(interaction: discord.Interaction):
        await interaction.response.send_message("With what do you want to gamble? choose from: dice, coin, number")

        def check(message):
            return message.author == interaction.user and message.channel == interaction.channel

        try:
            msg = await bot.wait_for('message', check=check, timeout=10)
        except:
            await interaction.followup.send("you took too long to respond")
            return

        user_id = str(interaction.user.id)
        if user_id not in user_xp:
            user_xp[user_id] = 0

        if msg.content == "dice":
            await interaction.followup.send(f'alright! , you will roll to dives, and if the numbers are the same you will get xp!')
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            if dice1 == 1 and dice2 == 1:
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

        elif msg.content == "coin":
            gamble = random.choice(["heads", "tails"])
            await interaction.followup.send(f'you flipped up a coin and got:{gamble}')
            if gamble == "heads":
                await interaction.followup.send("you earned 40 xp!")
                user_xp[user_id] += 40
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
                await interaction.followup.send(f'you have {user_xp[user_id]} xp')
            elif gamble == "tails":
                if user_xp[user_id] <= 0 or user_xp[user_id] < 20:
                    user_xp[user_id] = 0
                    await interaction.followup.send("you cant lose any xp!")
                else:
                    await interaction.followup.send("you lost 20 xp!")
                    user_xp[user_id] -= 20
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
                await interaction.followup.send(f'you have {user_xp[user_id]} xp')

        elif msg.content == "number":
            number = random.randint(1, 1000)
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
                if user_xp[user_id] <= 0 or user_xp[user_id] < 50:
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
                if user_xp[user_id] < 0 or user_xp[user_id] < 20:
                    user_xp[user_id] = 0
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
