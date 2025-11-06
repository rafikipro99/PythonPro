import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
@bot.command()
async def adivina(ctx):
    numero_secreto = random.randint(1, 10)
    await ctx.send("🎯 Adivina un número entre 1 y 10. ¡Escribe tu respuesta!")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

    try:
        mensaje = await bot.wait_for("message", check=check, timeout=10.0)
        eleccion = int(mensaje.content)

        if eleccion == numero_secreto:
            await ctx.send(f"🎉 ¡Correcto {ctx.author.name}! El número era {numero_secreto}.")
        else:
            await ctx.send(f"❌ No, el número era {numero_secreto}. ¡Sigue intentando!")
    except:
        await ctx.send("⌛ Se acabó el tiempo. ¡Tienes que responder más rápido!")
@bot.command()
async def ppt(ctx, eleccion: str = None):
    opciones = ["piedra", "papel", "tijeras"]
    if eleccion is None or eleccion.lower() not in opciones:
        await ctx.send("🪨 Usa el comando así: `!ppt piedra`, `!ppt papel` o `!ppt tijeras`")
        return
bot.run("Pon tu token")
