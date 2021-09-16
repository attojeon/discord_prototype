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
domain = 'https://cdn.discordapp.com/attachments'
image_urls = ['/883568550915223555/885067603675074580/788595ccdf65d51f.jpg',
             '/883568550915223555/884745201522999296/a807d1c33efdbc16.png',
             '/883568550915223555/883575289383378994/7946ea8b23c12cb5.jpg',
             '/883568550915223555/883568619328516167/16f2087c12d96b85.jpg'
             ]
# 명령은 /(슬래시)로 시작함. 
bot = commands.Bot(command_prefix='/', description=description, intents=intents) 

@bot.event
async def on_ready():
    print(title)
    print(f"{bot.user.name}님이 로그인 하셨습니다. --- \
          Id: {bot.user.id} 로그인시간: {datetime.now()}")
    print('-'*80)

# 사용법 : /add 10 20 =>두 수의 합을 말해줌
@bot.command(aliases=['더하기', '합'])
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

# 사용법 : /roll 3d10   => 10까지 수 중 3번 주사위 굴려! 
@bot.command(aliases=['주사위', '굴려'], description="주사위 굴리기")
async def roll(ctx, dice: str):
    # 명령이 형식에 맞는 지 확인
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('잘못된 명령')
        return

    dices = []
    for r in range(rolls):
        dices.append( str(random.randint(1, limit) ))
    result = ', '.join( dices )
    await ctx.send(result)

# 사용법 : /choose 1 2 3 4 5 6  
@bot.command(aliases=['선택'], description='선택하기')
async def choose(ctx, *choices: str):
    val = random.choice(choices)
    embed = discord.Embed(
        title="선택",
        description=f"당신의 선택 ==> {val}",
        url= config.cover_url,
        color=discord.Color.from_rgb(125, 125, 125))
    embed.set_thumbnail(url = domain + random.choice(image_urls))
    await ctx.send( embed= embed)

# 사용법 : /repeat 100 "아토쌤 사랑해요~"
@bot.command(aliases=['반복'])
async def repeat(ctx, times: int, content='반복내용...'):
    for i in range(times):
        await ctx.send(f"{i+1}: {content}")

bot.run( config.TOKEN)

'''
/add 명령어 예시 플러스
- 명령어 추가
- 명령어 대체이름 aliases 사용
- 리스트에서 이미지썸네일 사용 
'''