import discord
import random
import json
#continue to develop the rank system in gamble command

GUILD_ID = discord.Object(id=1468209555761532980)


def setup(bot, user_xp, rank_advance, user_rank):
    @bot.tree.command(name="game", description="play a game with the bot", guild=GUILD_ID)
    async def game_command(interaction: discord.Interaction):
        secret = random.randint(1, 10)
        await interaction.response.send_message("guess a number between 1 and 10")

        def check(message):
            return message.author == interaction.user and message.channel == interaction.channel

        try:
            msg = await bot.wait_for('message', check=check, timeout=10)
        except:
            await interaction.followup.send("you took too long to respond")
            return

        if msg.content == str(secret):
            await interaction.followup.send("you guessed the number correctly")
        else:
            await interaction.followup.send(f"you guessed the number incorrectly, it was {secret}")

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
        if user_id not in user_rank:
            user_rank[user_id] = 0
        if user_id not in rank_advance:
            rank_advance[user_id] = 50

        async def check_rank_up():
            if user_xp[user_id] >= rank_advance[user_id]:
                user_rank[user_id] += 1
                rank_advance[user_id] += 50
                await interaction.followup.send(f"you advanced to rank {user_rank[user_id]}!")
                with open("rank.json", "w") as f:
                    json.dump(user_rank, f)
                with open("rank_advance", "w") as f:
                    json.dump(rank_advance, f)

        if msg.content == "dice":
            await interaction.followup.send('alright! you will roll two dice, and if the numbers are the same you will get xp!')
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            if dice1 == dice2:
                xp_earned = dice1 * 10
                await interaction.followup.send(f'you rolled a double {dice1}! you earned {xp_earned} xp!')
                user_xp[user_id] += xp_earned
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
                await check_rank_up()
            else:
                await interaction.followup.send(f'you rolled a {dice1} and a {dice2}, you didn\'t earn any xp!')
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')

        elif msg.content == "coin":
            gamble = random.choice(["heads", "tails"])
            await interaction.followup.send(f'you flipped a coin and got: {gamble}')
            if gamble == "heads":
                await interaction.followup.send("you earned 40 xp!")
                user_xp[user_id] += 40
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
                await check_rank_up()
            elif gamble == "tails":
                if user_xp[user_id] < 20:
                    user_xp[user_id] = 0
                    await interaction.followup.send("you can't lose any xp!")
                else:
                    user_xp[user_id] -= 20
                    await interaction.followup.send("you lost 20 xp!")
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')

        elif msg.content == "number":
            number = random.randint(1, 1000)
            await interaction.followup.send(f'you received the number: {number}')
            if number == 666:
                await interaction.followup.send("you received the devil number! you earned 30 xp!")
                user_xp[user_id] += 30
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
                await check_rank_up()
            elif number == 667:
                await interaction.followup.send("you received 667! you earned 100 xp!")
                user_xp[user_id] += 100
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
                await check_rank_up()
            elif number == 67:
                await interaction.followup.send("you received 67! you earned 120 xp!")
                user_xp[user_id] += 120
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
                await check_rank_up()
            elif number == 777:
                await interaction.followup.send("you received the lucky number! you earned 50 xp!")
                user_xp[user_id] += 50
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
                await check_rank_up()
            elif number == 900:
                if user_xp[user_id] < 50:
                    await interaction.followup.send("you received the unlucky number! you can't lose any xp!")
                    user_xp[user_id] = 0
                else:
                    await interaction.followup.send("you received the unlucky number! you lost 50 xp!")
                    user_xp[user_id] -= 50
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
            elif number == 1000:
                await interaction.followup.send("you received the max number! you earned 200 xp!")
                user_xp[user_id] += 200
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
                await check_rank_up()
            elif number == 1:
                if user_xp[user_id] < 20:
                    user_xp[user_id] = 0
                    await interaction.followup.send("you received the min number! you can't lose any xp!")
                else:
                    user_xp[user_id] -= 20
                    await interaction.followup.send("you received the min number! you lost 20 xp!")
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
            elif number == 500:
                await interaction.followup.send("you received the middle number! you earned 20 xp!")
                user_xp[user_id] += 20
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
                await check_rank_up()
            elif number == 250:
                await interaction.followup.send("you received the quarter number! you earned 10 xp!")
                user_xp[user_id] += 10
                with open("xp.json", "w") as f:
                    json.dump(user_xp, f)
                await check_rank_up()
            else:
                await interaction.followup.send("you didn't receive any special number, you didn't earn or lose any xp!")
            await interaction.followup.send(f'you have {user_xp[user_id]} xp')
