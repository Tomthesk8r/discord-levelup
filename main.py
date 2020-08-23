import discord
import random
import string
import asyncio
import os
import json
from colorama import Fore


from discord.ext import (
    commands,
    tasks
)

client = discord.Client()
client = commands.Bot(
    command_prefix="!",
    self_bot=True
)
client.remove_command('help')

with open('config.json') as f:
    config = json.load(f)
    
token = config.get("token")




def Init():
    if config.get('token') == "token-here":
        os.system('cls')
        print(f"\n\n{Fore.RED}Error {Fore.WHITE}You didnt put your token in the config.json file\n\n"+Fore.RESET)
        exit()
    else:
        token = config.get('token')
        try:
            client.run(token, bot=False, reconnect=True)
            os.system(f'Discord LevelUpBot')
        except discord.errors.LoginFailure:
            print(f"\n\n{Fore.RED}Error {Fore.WHITE}Token is invalid\n\n"+Fore.RESET)
            exit()



def random_symbols(length):
    return ''.join(random.choice(string.ascii_uppercase) for i in range(length))

os.system('cls')
print(f"{Fore.GREEN}Bot is ready")
print(f"{Fore.WHITE}Write {Fore.YELLOW}!levelup <number of messages>{Fore.WHITE} to start level up")


@client.command()
async def levelup(ctx,amount: int):
    await ctx.message.delete()
    msgsend = amount
    print(f"{Fore.YELLOW}Sending {msgsend} messages\n\n")
    while msgsend > 0:
        msgsend -= 1
        print(f"{Fore.YELLOW}Messages left to send: {Fore.WHITE}{msgsend}")
        if msgsend == 0:
            print(f"\n{Fore.GREEN}All messages was sent")
        output = random_symbols(5) + "-" + random_symbols(5) + " " + random_symbols(5) + "-" + random_symbols(5) + " " + random_symbols(5)
        try:
            await ctx.send(output)
        except:
            print(f"{Fore.RED}Error: {Fore.WHITE}Cannot send message #{msgsend}")
            pass
        await asyncio.sleep(1)
        async for message in ctx.message.channel.history(limit=1).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                print(f"{Fore.RED}Error: {Fore.WHITE}Cannot delete message #{msgsend}")
                pass
        await asyncio.sleep(60)
    return

@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}Error: {Fore.WHITE}Discord error: {error}"+Fore.RESET)    
    else:
        print(f"{Fore.RED}Error: {Fore.WHITE}{error_str}"+Fore.RESET)

Init()
