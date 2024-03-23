import discord
import random
import asyncio

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Connesso come {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/sasso_carta_forbice'):
        tua_scelta = message.content.split()[1].upper()
        if tua_scelta not in ["SASSO", "CARTA", "FORBICE"]:
            await message.channel.send("Scelta non valida. Devi scegliere tra SASSO, CARTA o FORBICE.")
            return

        # Messaggio iniziale
        await message.channel.send("Sasso, Carta, Forbice inizia tra 3...")
        await asyncio.sleep(1)
        await message.channel.send("2...")
        await asyncio.sleep(1)
        await message.channel.send("1...")
        await asyncio.sleep(1)

        # Scegli una delle opzioni casualmente
        scelte = ["SASSO", "CARTA", "FORBICE"]
        scelta_bot = random.choice(scelte)

        # Invia la scelta del bot
        await message.channel.send(scelta_bot)

        # Determina il risultato del gioco
        if tua_scelta == scelta_bot:
            await message.channel.send("Pareggio!")
        elif tua_scelta == "FORBICE" and scelta_bot == "SASSO":
            await message.channel.send("TI HO BATTUTO!")
        elif tua_scelta == "SASSO" and scelta_bot == "FORBICE":
            await message.channel.send("HAI VINTO!")
        elif tua_scelta == "CARTA" and scelta_bot == "FORBICE":
            await message.channel.send("HAI VINTO!")
        elif tua_scelta == "FORBICE" and scelta_bot == "CARTA":
            await message.channel.send("TI HO BATTUTO!")
        elif tua_scelta == "SASSO" and scelta_bot == "CARTA":
            await message.channel.send("TI HO BATTUTO!")
        elif tua_scelta == "CARTA" and scelta_bot == "SASSO":
            await message.channel.send("HAI VINTO!")

    elif message.content.startswith('/ciao'):
        await message.channel.send("e sti cabbi")

# Inserisci il tuo token del bot Discord qui
TOKEN = 'token_here'

client.run(TOKEN)
