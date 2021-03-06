import os
import discord
from discord import channel
import requests
from discord.ext import commands
from emotion_detection import Emotion_detection
from dotenv import load_dotenv
from hdi import Hdi
from topic_sentiment import Topic_sentiment

load_dotenv()

#Gerimbots
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', description='description', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):

    clown_emoji = '\U0001F921'
    love_emoji = '\U0001F970'
    fear_emoji = '\U0001F61F'
    happy_emoji = '\U0001F601'
    anger_emoji = '\U0001F621'
    sad_emoji = '\U0001F622'
    surprised_emoji = '\U0001F62E'

    await bot.process_commands(message)
    
    # TODO initialize Malaya so that deployment will be faster
    if not message.author.bot:
        emotion = Emotion_detection().getEmotion([message.content])

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

@bot.command(name='hdi')
async def hdi(ctx, *, question):
    result = Hdi().execute(question)

    await ctx.send(result)

@bot.command(name='analyze')
async def analyze(ctx, *, topic):
    result = Topic_sentiment().analyze_tweet(topic)
    print(result)

    await ctx.send(result)

@bot.command()
async def test(ctx, args1):
    await ctx.send(args1)

def getData(url):
    r = requests.get(url)
    return r.text

bot.run(TOKEN)

