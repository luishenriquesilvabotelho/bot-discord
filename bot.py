import discord
from discord.ext import commands
import requests
import pandas as pd

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.command()
async def oi(ctx):
    await ctx.send('oi!')
@bot.command()
async def jogo(ctx, jogo):
    url=f"https://store.steampowered.com/api/appdetails?appids={jogo}&l=brazilian"
    headers = {
        "accept" : "application/json"
    }

    response = requests.get(url, headers=headers)
    dataframe = pd.read_json(response.text)

    foto=dataframe[int(jogo)]['data']['capsule_image'].replace('\\', '')
    await ctx.send(foto)
    print(dataframe)

    texto = "\n ```"
    texto+= f'\nJogo:'+dataframe[int(jogo)]["data"]["name"]
    descricao_jogo = dataframe[int(jogo)]["data"]["short_description"]
    texto += f'\n\n{descricao_jogo} \n\n'
    if "price_overview" in dataframe[int(jogo)]['data']:
        desconto = dataframe[int(jogo)]["data"]["price_overview"]['discount_percent']
        if(desconto>0):
            texto += '\nDesconto de'+ str(desconto)+ "$"
        else:
            texto += "\nSem desconto"
        preco = dataframe[int(jogo)]['data']['price_overview']['final_formatted']
        texto+=f'\nPreço:' +preco
    else:
        texto += '\nDe graça'
    texto+= '\n```'

    await ctx.send(texto)
bot.run('MTI5NjI1NzQxNjU5MzQxMjIxNg.GSlJti.M1ulJyH-gC8kCojwd8RUfP1OIlSo1ociKGr6rQ')