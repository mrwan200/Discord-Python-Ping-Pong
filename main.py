from discord.ext import commands

bot = commands.Bot(command_prefix="")

@bot.event
async def on_ready(): # เช็คว่าบอทออนไลน์หรือยัง
    print("Bot ready.") # ถ้าบอททำงาน คำสั่งนี้(print) จะทำงาน 

@bot.event
async def on_message(message): # ใส่คำที่ให้ผู้ใช้งานป้อน
    if message.content == ">ping": # ใส่คำที่บอทตอบกลับ
        await message.channel.send("Pong.")
        # ถ้าUser พิมพ์ >ping บอทจะตอบกลับว่า pong

bot.run("YOUR BOT TOKEN HERE") # ใส่โทเคนของบัญชีที่จะให้บอทไปสิง
