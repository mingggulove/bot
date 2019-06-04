import discord
import random
import requests
client = discord.Client()

@client.event
async def on_ready():
   print(client.user.id)
   print("ready")



@client.event
async def on_message(message):
 if message.content.startswith("도와줘"):
   await message.channel.send("여기로오면되요! https://discord.gg/gYakJwg")
 if message.content.startswith("질문이야"):
   await message.channel.send("난 아직한글 잘모르겠어ㅜ")
 if message.content.startswith("나좋아?"):
   await message.channel.send("좋아요!")
 if message.content.startswith("모모야"):
   await message.channel.send("저찾으셨나요?히히")


client.run('NTg1MjU0NjUyMTI0MjAwOTY0.XPXDcw.SCh26DdyPMiXCzmutsGxaxQaeaA')