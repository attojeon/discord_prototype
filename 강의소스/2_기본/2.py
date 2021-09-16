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
    print('-'*80)

# 사용법 : /add 10 20 =>두 수의 합을 말해줌
@bot.command()
async def add(ctx, left: int, right: int):
    c = discord.Color.from_rgb(0, 0, 255)
    val = left + right
    embed=discord.Embed(
        title="두 수의 합",
        description=f"{left} + {right} = {val}",
        url= config.cover_url,
        color=c)
    embed.set_image(url = config.cover_url)
    # embed.set_thumbnail(url = config.cover_url)
    await ctx.send(embed = embed)

bot.run( config.TOKEN)

'''
/add 명령어 예시 플러스
- 링크 걸기
- 인터넷 url 이미지 보여주기
- 인터넷 url 썸네일 보여주기 
- 대화라인의 색상 추가하기 
'''