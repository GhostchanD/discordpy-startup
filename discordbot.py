from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='+')
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_ready():
  print("logged in as " + client.user.name)

@client.event
async def on_message(message):
  if message.author != client.user:
    msg = message.author.mention + " Hi."
    await client.send_message(message.channel, msg)

    
bot.run(token)
