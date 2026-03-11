import discord
from googletrans import Translator

TOKEN = "MTQ4MTMwODgwOTY5ODc0MjM2Mw.Gon-lo.dBNzHeEhLjlSIstP8Ab5MdFpzdZ1-OCRCXgAZ4

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
translator = Translator()

@client.event
async def on_ready():
    print("Bot đã online")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    translated = translator.translate(message.content, dest="vi")
    await message.channel.send(translated.text)

client.run(TOKEN)