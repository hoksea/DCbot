import discord
import os
import time
# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']

client = discord.Client()

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')

# 收到訊息時呼叫
@client.event
async def on_message(message):
    if message.content == '早':
        channel = message.channel
        await message.channel.send('早安喔')

# Bot起動
client.run(TOKEN)
