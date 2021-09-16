import discord
from discord.ext import commands
import random
from datetime import datetime
import config 

intents = discord.Intents.default()
intents.members = True
description = '''디스코드봇을 만들기 위한 샘플 코드'''
title = '''
                  //\\
         /|   (' )/\\\\
<---<< = | >()HJH \\\\
         \\|     \\ _\\_
               //____|J
'''

# 명령은 /(슬래시)로 시작함. 
bot = commands.Bot(command_prefix='/', description=description, 
                   intents=intents) 

@bot.event
async def on_ready():
    print(title)
    print(f"{bot.user.name}님이 로그인 하셨습니다. --- \
          Id: {bot.user.id} 로그인시간: {datetime.now()}")
    print('#'*80)

# 사용법 : /add 10 20 =>두 수의 합을 말해줌
@bot.command()
async def add(ctx, left: int, right: int):
    val = left + right
    embed=discord.Embed(
        title="두 수의 합",
        description=f"{left} + {right} = {val}" )
    await ctx.send(embed = embed)

bot.run( config.TOKEN)

'''
/add 명령어 예시 
'''