import os
import discord
from discord import channel
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import random
import twint
#from twint_service import twint_service
import malaya

TOKEN = "NzMyMjExNjczNzMzMjY3NTY2.XwxTQg.0YupVDaWehMBGKld91R6Pql5vCU"
werewolf_general_channelId = 683682244434460784
swuack_general__channelId = 713423084807520290

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description='description', intents=intents)

model = malaya.emotion.multinomial()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


async def send_message(message='test'):
    channel = bot.get_channel(683682244434460784)
    await channel.send(message)

@bot.event
async def on_message(message):

    clown_emoji = '\U0001F921'
    love_emoji = '\U0001F970'
    fear_emoji = '\U0001F61F'
    happy_emoji = '\U0001F601'
    anger_emoji = '\U0001F621'
    sad_emoji = '\U0001F622'
    surprised_emoji = '\U0001F62E'

    channel = bot.get_channel(werewolf_general_channelId)
    emotion = model.predict([message.content])

    print(emotion)
    
    if emotion == ['love']:
        await message.add_reaction(love_emoji)
    elif emotion == ['fear']:
        await message.add_reaction(fear_emoji)
    elif emotion == ['happy']:
        await message.add_reaction(happy_emoji)
    elif emotion == ['anger']:
        await message.add_reaction(anger_emoji)
    elif emotion == ['sadness']:
        await message.add_reaction(sad_emoji)
    elif emotion == ['surprise']:
        await message.add_reaction(surprised_emoji)
    else:
        await message.add_reaction(clown_emoji)

    with open("DISCORD_CONVERSATION(EMOTION).txt", "a+") as file_object:
        # Append 'hello' at the end of file
        file_object.write(message.content + "\t" + str(emotion) + "\n")
        

    if '!meme' in message.content:
        print('Someone asked for meme')

        # Do stuff here
        channel = bot.get_channel(werewolf_general_channelId)
        html_data = getData('https://www.memecenter.com/')
        soup = BeautifulSoup(html_data, 'html.parser')

        #TODO revisit algorithm
        hot_memes = []

        for item in soup.find_all('img'):
            hot_memes.append(item['src'])

        await channel.send(random.choice(hot_memes))

    if '!party' in message.content:
        print('Protocol party')

        # Do stuff here
        channel = bot.get_channel(werewolf_general_channelId)
        html_data = getData('https://www.memecenter.com/')
        soup = BeautifulSoup(html_data, 'html.parser')

        hot_memes = []

        for item in soup.find_all('img'):
            hot_memes.append(item['src'])
        
        for i in range(5):
            await channel.send(random.choice(hot_memes))

    if '!help' in message.content:
        # Do stuff here
        channel = bot.get_channel(werewolf_general_channelId)
        await channel.send("! meme for A meme\n! party for some memes\n! analyze using malaya emotion detection")

    #TODO fix this shit
    if '!tweet' in message.content and len(str(message.content).split()) > 1:
        channel = bot.get_channel(swuack_general__channelId)
        message = str(message.content).split()
        username = message[1]

        twitInfo = twint_service()
        print(twitInfo)
  
        await channel.send(twint_service())
    
    if '!analyze' in message.content and len(str(message.content).split()) > 1:
        print('MALAYA ONZ')

        channel = bot.get_channel(werewolf_general_channelId)
        analyze_text = str(message.content).strip('!analyze')

        emotion = model.predict([analyze_text])
        print("okay")
        await channel.send(emotion)

def getData(url):
    r = requests.get(url)
    return r.text

bot.run(TOKEN)

