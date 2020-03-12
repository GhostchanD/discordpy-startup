from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def serverinfo(ctx):
    await ctx.send('サーバー全体の役職')
    await ctx.send('%message.guild.members%')
    await ctx.send('あなたの役職')
    print(message.guild.roles)
    
@bot.command()
async def helpcommand(ctx):
    await ctx.send('/serverinfo <-サーバーの詳細')
    await ctx.send('/test <-debug')
    await ctx.send('/helpcommand <-commandlist')
    
@bot.command()
async def test(ctx):
    await ctx.send('test world 1')
    await ctx.send('test world 2')
    await ctx.send('test world 3')
    await ctx.send('test world 4')


bot.run(token)
