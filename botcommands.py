# This example requires the 'members' privileged intents

import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

# 명령은 .(점) 으로 시작함. 
bot = commands.Bot(command_prefix='/', description=description, intents=intents) 

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(aliases=['.', 't'])
async def shortwords(ctx):
    responses = [
        "영고 : 영원한 고통",
        "일상가: 일상 생활 가능",
        "취준: 취향 존중",
        "마상: 마음의 상처",
        "혼코노: 혼자코인 노래방",
        "얼죽아: 얼어죽어도 아이스 아메리카노",
        "팬아저: 팬 아니어도 저장",
        "제곧내: 제목이 곧 내용",
        "별다줄: 별걸 다 줄인다",
        "애빼시: 애교 빼면 시체",
        "뼈뚜맞: 뼈로 뚜두려 맞았다",
        "팩력배: 팩트 + 폭력배",
        "너또다: 너도 또라이라 다행이다",
        "고스팅: 유령처럼 연락이 두절되다",
        "멍청비용: 나의 부주의로 뜻하지 않게 낭비하게 되는 돈",
        "펭하: 펭수 하이",
        "ASKY: (애인, 돈) 안생겨요",
        "현시창: 현실은 시궁창",
        "핑프: 핑거 프린세스",
        "쪘잘싸: 쪘지만 잘 싸웠다",
        "나심비: 나의 심리적인 가성비는 좋다",
        "인싸: 인사이더",
        "꾸안꾸: 꾸민 듯 안 꾸민듯",
        "된찌/부찌: 된장찌게, 부대찌게",
        "남나깡: 남자는 나이가 깡패다, 어릴 수록 좋다",
        "미먼: 미세먼지",
        "자낳괴: 자본주의가 낳은 괴물",
        "빼박: 빼도박도 못한다",
        "자강두천: 자존심이 강한 두 천재",
        "뇌피셜: 검증된 사실이 아닌 자신의 생각만을 근거로 한 주장이나 추측",
        "빌런: 악당에서 유래, 무언가에 집착하거나 특이한 행동을 하는 사람",
        "현피: 현실 PK, 게임에서 시비가 붙어서 실제로 만나서 싸우는 일",
        "워라블: 워크 라이프 블랜딩, 일과 삶을 분리하지 않고 잘 섞어야 한다",
        "우유남: 우월한 유전자를 가진 남자",
        "썁파서블: 매우 가능하다",
        "내또출: 내일 또 출근",

    ]

    await ctx.send( random.choice(responses))

# 사용법 : .add 10 20 
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# 사용법 : .roll 3d10   => 10까지 수 중 3번 주사위 굴려! 
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

# 사용법 : choose 1 2 3 4 5 6  
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

# 사용법 : .repeat 100 "아토쌤 사랑해요~"
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

# bot.run('ODA3ODQzNjAxNTY4NDk3Njg0.YB94-w.45kw55Pw3k4qwv-0ePVKQuS3nuE')
bot.run( 'ODQxMjQ0MDU0NTc0NTk2MTI4.YJj7lA.441sAFiYq3uSsE8ZlF7fFXNfY4o')