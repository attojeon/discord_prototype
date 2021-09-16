import discord
from discord.ext import commands
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random
import config 
import time 

COM_NODE = '명령어'
RES_NODE = '자원'
USR_NODE = '회원'
ResList = None
RandomMine = []

def show_node(node_name):
    dir = db.reference(node_name)
    node = dir.get()
    if type(node) == dict:
        for k, v in node.items():
            print(f"{k}: {v}")    
    elif type(node) == list:
        for v in node:
            print(f"v: {v}")

def user_init(user):
    name, code = str(user).split('#')
    username = name + code 
    print(f"n:{name}, c:{code}, username: {username}")
    dir_user = db.reference(USR_NODE + '/' + username)
    dir_user.update({"name":name,"code":code, 
                     "가입":time.strftime('%Y/%m/%d %H:%M:%S')})

    migration_user(username)

def get_resourcelist():
    res_list = db.reference(RES_NODE).get().keys()
    res_base = {}
    for r in res_list:
        res_base[r] = 0
    print(f"res_base: {res_base}")
    return res_base

def migration_user(user):
    dir= db.reference(USR_NODE)
    dir_pack = db.reference(USR_NODE + '/' + user + "/보석함")
    items = get_resourcelist()
    dir_pack.update(items) 
    print(f"migration_user: ${items}") 

def mine_init():
    dir_mine = db.reference(RES_NODE).get()
    for mine_name, content in dir_mine.items():
        for n in range( content['rate'] ):
            RandomMine.append(mine_name)
    random.shuffle( RandomMine )
    print(f"mine count:{len(RandomMine)}, mine: {RandomMine}")

def user_mining(username, stone, qty):
    print(f"username: {username}, stone: {stone}, qty:{qty}")
    stone_node = f"{USR_NODE}/{username}/보석함/{stone}"
    stock = db.reference(stone_node).get()
    new_qty = int(stock) + qty
    db.reference(f"{USR_NODE}/{username}/보석함").update({stone: new_qty})

# DB connection & settings
cred = credentials.Certificate(config.firebase_secret_file)
firebase_admin.initialize_app(cred, {'databaseURL' : config.firebase_url})
ResList = get_resourcelist()
mine_init()

# Discord Init & settings 
intents = discord.Intents.default()
intents.members = True
description = '''골드마인드 with 디스코드봇'''
title = '''골드마인드 with 디스코드봇'''
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
          Id: {bot.user.id} 로그인시간: {time.asctime( time.localtime())}")
    print('-'*80)

@bot.event 
async def on_member_join(member):
    print(member)
    user_init(member)  #런스팀#5591
    await member.guild.system_channel.send(f"{member}님 가입을 환영합니다.")
    # await member.send("안녕하세요, 가입을 환영합니다.")

# 사용법 : /add 10 20 =>두 수의 합을 말해줌 
@bot.command(aliases=['광질', '채광'])
async def mine(ctx):
    c = discord.Color.from_rgb(0, 0, 255)
    stone = random.choice( RandomMine )
    qty = random.choice( [1, 1, 1, 1, 1, 1, 1, 1, 1, 2] )
    embed=discord.Embed(
        title=f"당신은 {stone} {qty}개를 캤습니다.",
        description=f"=== 채굴 결과 ===",
        color=c)
    embed.set_thumbnail(url = domain + image_urls[0])

    # db update 
    username = ctx.author.name + ctx.author.discriminator
    user_mining(username, stone, qty)

    await ctx.send( embed=embed )


# 사용법 : /repeat 100 "아토쌤 사랑해요~"
@bot.command(aliases=['판매'])
async def repeat(ctx, stone: str, qty: int):
    pass
    await ctx.send(f"{stone}: {qty}")

bot.run( config.TOKEN)

'''
/add 명령어 예시 플러스
- 명령어 추가
- 명령어 대체이름 aliases 사용
- 리스트에서 이미지썸네일 사용 
'''