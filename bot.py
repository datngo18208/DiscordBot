import discord
import os

TOKEN = os.getenv("MTQ4MTMwODgwOTY5ODc0MjM2Mw.GYSRqx.4u6YXJoxu7XimBmGxAhkNE9jeFa8WJtrT9ldaE")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot đã online: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!ping":
        await message.channel.send("pong 🏓")

client.run(TOKEN)