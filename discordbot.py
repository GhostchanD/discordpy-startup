import requests
import json
import discord
from discord.ext import commands

discord_TOKEN = 'NTQ2MzE2NjIzNzI5MDAwNDc5.Xmy8JA.4ki5rZa6-f9TgRLnXiguIV79Yo8' #ここにdiscordBotのTOKEN
alteing_APIKEY = "api-a831-0f11-c62b" #ここにalteningのAPIKEY
channel = 338289770230710284 #ここはGHのbot-commandのチャンネルID

client = discord.Client()
bot = commands.Bot(command_prefix='/')

# 起動時に動作する処理
@client.event #何故か機能しない
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
   print('ログインしました')

@bot.command(name="gen")
async def account_check(ctx):
    if ctx.channel.id != channel:
        await ctx.send("そのチャンネルでは使用できません")
        await ctx.message.delete()
        return
    url = f"http://api.thealtening.com/v1/generate?token={alteing_APIKEY}&info=true" #URLにアクセス ""の前のfは{}で変数を使えるようになるやつ  generate?token= + altening_APIKEYをしなくてもよくなる
    r = requests.get(url) #URL先の文字をゲットする {"token": "aiodhsoa","name": "osdjaij"}とかの文字
    data = r.json() #文字を辞書型にする (辞書型は調べといて)
    if data["limit"] == "true": #もしlimitがtrueだったらメッセージを出す
        await ctx.send("一日のリミットに達しました")
        return
    embed = discord.Embed(title="Thealteing Generater",description="how to user -> /gen",color=discord.Colour.blue()) #embed作る
    token = data["token"] #alteningのTOKENを変数に入れる
    embed.add_field(name="Token",value=data["token"]) #embedの項目を増やす alteningのtokenをvalueに入れる
    if "hypixel.lvl" in data["info"]: #もしハイピクセルレベルがあったら
        lv = data["info"]["hypixel.lvl"] #変数に入れて
        embed.add_field(name="Hypixel Lv",value=lv) #embedに追加
    if "hypixel.rank" in data["info"]: #後同じ
        rank = data["info"]["hypixel.rank"]
        embed.add_field(name="Hypixel Rank",value=rank)
    if "mineplex.lvl" in data["info"]:
        mineplex_lv = data["info"]["mineplex.lvl"]
        embed.add_field(name="Mineplex Lv",value=mineplex_lv)
    if "mineplex.rank" in data["info"]:
        mineplex_rank = data["info"]["mineplex.rank"]
        embed.add_field(name="Mineplex Rank",value=mineplex_rank)
    if "labymod.cape" in data["info"]:
        laby_cape = data["info"]["labymod.cape"]
        embed.add_field(name="Labymod Cape",value=laby_cape)
    if "5zig.cape" in data["info"]:
        zig_cape = data["info"]["5zig.cape"]
        embed.add_field(name="5zig Cape",value=zig_cape)
    await ctx.send(embed=embed) #最後にembed送信！！


bot.run(discord_TOKEN)
