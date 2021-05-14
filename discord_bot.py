import discord 
from discord.ext import commands 
import random 
import open_weather
import config

client = commands.Bot(command_prefix='.')
TOKEN = config.TOKEN

@client.event 
async def on_ready():
    print("봇2이 준비되었습니다.")

@client.event
async def on_member_join(member):
    print(f"{member}가 서버에 접속하였습니다.")

@client.event 
async def on_member_remove(member):
    print(f"{member}가 접속을 해제하였습니다.")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong2! {round( client.latency * 1000)} ms")

@client.command(aliases=['8ball', 'test', '아무거나']) 
async def _8ball(ctx, *, question):
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
    await ctx.send(f"질문2: {question}\n대답: {random.choice(responses)} ")

'''
embed.set_thumbnail(url='')
embed.set_author(name='', icon_url='')
embed.add_field(name='field 1 title', value='description', inline=False)
embed.set_footer(text='')

ctx.author.display_name
ctx.author.avatar_url

'''
@client.command(aliases=['날씨', 'weather']) 
async def _weather(ctx, *, question):
    response = open_weather.predict_weather(question)
    embed_msg = discord.Embed(title="날씨 조회 서비스", url="", description=response, color=0xFF5733)
    embed_msg.set_author(name="ato",icon_url="http://learnsteam.co.kr/kbd/wp-content/uploads/2017/09/robots.png")
    # await ctx.send(f"지역 날씨: {question}\n결과: {response}")
    await ctx.send(embed=embed_msg)

client.run(TOKEN)