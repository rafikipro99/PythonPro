import discord
from discord.ext import commands
import random

# --- CONFIGURACIÓN DEL BOT ---
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# --- EVENTO CUANDO EL BOT SE CONECTA ---
@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# --- COMANDO DE AYUDA PERSONALIZADO ---
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="📘 Lista de comandos del bot",
        description="Aquí tienes todos los comandos disponibles:",
        color=discord.Color.blue()
    )

    embed.add_field(name="🎮 Juegos", value=(
        "`!adivina` — Adivina un número del 1 al 10\n"
        "`!ppt` — Juega piedra, papel o tijeras contra el bot\n"
        "`!dado` — Tira un dado (1 al 6)"
    ), inline=False)

    embed.add_field(name="ℹ️ Información", value=(
        "`!help` — Muestra esta lista de comandos\n"
        "`!ping` — Verifica la latencia del bot"
    ), inline=False)

    embed.set_footer(text="🤖 Bot hecho en Python con py-cord")
    await ctx.send(embed=embed)

# --- COMANDO PING ---
@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! Latencia: {round(bot.latency * 1000)}ms")

# --- JUEGO: ADIVINA EL NÚMERO ---
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

# --- JUEGO: PIEDRA, PAPEL O TIJERAS ---
@bot.command()
async def ppt(ctx, eleccion: str = None):
    opciones = ["piedra", "papel", "tijeras"]
    if eleccion is None or eleccion.lower() not in opciones:
        await ctx.send("🪨 Usa el comando así: `!ppt piedra`, `!ppt papel` o `!ppt tijeras`")
        return

    bot_eleccion = random.choice(opciones)
    await ctx.send(f"🤖 Yo elijo **{bot_eleccion}**")

    if eleccion == bot_eleccion:
        await ctx.send("😐 Empate.")
    elif (
        (eleccion == "piedra" and bot_eleccion == "tijeras") or
        (eleccion == "papel" and bot_eleccion == "piedra") or
        (eleccion == "tijeras" and bot_eleccion == "papel")
    ):
        await ctx.send("🎉 ¡Ganaste!")
    else:
        await ctx.send("💀 Perdiste...")

# --- JUEGO: DADO ---
@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)
    await ctx.send(f"🎲 Sacaste un **{numero}**")

# --- EJECUTAR BOT ---
bot.run("TU_TOKEN_AQUI")
