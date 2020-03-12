from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='+')
token = os.environ['DISCORD_BOT_TOKEN']


@client.event()
async def on_message(message):
    if message.author != client.user:
        msg = message.author.mention + " HEY "
        await client.send_message(message.channel, msg)
        
@bot.command()
async def test(ctx):
    await ctx.send('test world 1')
    await ctx.send('test world 2')
    await ctx.send('test world 3')
    await ctx.send('test world 4')
    
bot.run(token)
