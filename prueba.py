import discord
from discord.ext import commands
import datetime

mybot = commands.Bot(
    command_prefix="$", description="Bot de discord para descargar videos de YT :D")


@mybot.command()
# Async y await son parte de la implementacion de corutinas
async def ping(ctx):
    await ctx.send('pong')

# evento, que se realiza cuando sucede alguna accion
# En este caso cuando se conecta el bot


@mybot.event
async def on_ready():
    await mybot.change_presence(activity=discord.Streaming(name="owo", url="https://www.twitch.tv/rubius"))
    print("el bot llego B)")

# ahora procederemos a añadir commandos a nuestro bot
# por ejemplo una funcionalidad que sume cuando se le pase coomo comando
# recordar que el comando es con simbolo ! , esto fue programado mas arriba


@mybot.command()
async def suma(ctx, num1: int, num2: int):  # tienen que ser enteros
    await ctx.send(num1 + num2)


@mybot.command()
async def info(ctx):
    embed = discord.Embed(
        title=f"{ctx.guild.name}", description="solo c que nada c", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="El server fue creado en: ",
                    value=f"{ctx.guild.created_at}")
    embed.add_field(name="Dueño del server B): ",
                    value=f"{ctx.guild.owner}")
    await ctx.send(embed=embed)

# mybot.run('aqui va el hash de tu bot') #copiar del server de discvord antes de descomentar esto
