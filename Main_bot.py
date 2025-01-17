import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')


@bot.command("consejos")
async def consejos(ctx):
    consejos = [ "1. Separa correctamente los materiales: Asegúrate de separar plástico, papel, vidrio y metales, y límpialos antes de reciclar.",
    "2. Conoce los símbolos de reciclaje: Familiarízate con los símbolos para saber qué se puede reciclar y cómo.",
    "3. Evita reciclar productos contaminados: No pongas materiales sucios (como cajas de pizza manchadas) en los contenedores de reciclaje.",
    "4. Haz compost con residuos orgánicos: Recicla restos de comida en un compostador, si es posible.",
    "5. Recicla solo lo reciclable: No pongas productos no reciclables como plásticos de un solo uso o materiales mixtos.",
    "6. Reutiliza cuando sea posible: Dale una segunda vida a frascos, cajas y otros materiales.",
    "7. Participa en programas de reciclaje local: Infórmate sobre programas para reciclar pilas, electrónicos y ropa.",
    "8. Compra productos reciclados: Elige productos fabricados con materiales reciclados para apoyar el reciclaje.",
    "9. Reducción y reutilización antes que reciclaje: Reduce el consumo y reutiliza antes de pensar en reciclar.",
    "10. Organiza un espacio para reciclar en casa: Establece un sistema claro para separar los materiales reciclables."]
    await ctx.send(random.choice(consejos))

