from discord.ext import commands

bot = commands.Bot(command_prefix="")

@bot.event
async def on_ready():
    print("Bot ready.")

@bot.event
async def on_message(message):
    if message.content == ">ping":
        await message.channel.send("Pong.")

bot.run("ODYzNDI0ODcxOTI0MjM2Mjg5.YOmtEw.ksKpU3epIew38MQRRjXKzGUH_LE")