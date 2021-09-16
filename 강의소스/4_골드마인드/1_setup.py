import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import config 
import time 

COM_NODE = '명령어'
RES_NODE = '자원'
USR_NODE = '회원'
ResList = None

cred = credentials.Certificate(config.firebase_secret_file)
firebase_admin.initialize_app(cred, {'databaseURL' : config.firebase_url})

def user_init(user):
    name, code = str(user).split('#')
    username = name + code 
    print(f"n:{name}, c:{code}, username: {username}")
    dir_user = db.reference(USR_NODE + '/' + username)
    dir_user.update({"name":name,"code":code,"가입":time.strftime('%Y/%m/%d %H:%M:%S')})

    migration_user(username)

def get_resourcelist():
    res_list = db.reference(RES_NODE).get().keys()
    res_base = {}
    for r in res_list:
        res_base[r] = 0
    print(f"res_base: {res_base}")
    return res_base

def migration_user(user):
    dir_pack = db.reference(USR_NODE + '/' + user + "/보석함")
    items = get_resourcelist()
    dir_pack.update(items)
    print(f"migration_user: ${items}")

def migration():
    # 명령어 노드 추가
    commands = {}
    dir = db.reference('명령어')
    commands['회원가입'] = '회원가입 명령어로 데이터베이스에 데이터를 저장합니다'
    commands['이메일등록'] ='무단 로그인 방지를 위해 이메일을 등록하셔야 됩니다! 이메일등록은 사람이 없는곳에서 해주세요!'
    commands['로그인'] ='만약 자신이 아이디를 바꾸었을때 로그인으로 아이디를 찾을수 있습니다!'
    commands['지갑'] ='자신이 가진 돈을 보실수 있습니다'
    commands['광질'] ='광질을 하여 xp,광물을 얻으실수 있습니다'
    commands['판매'] ='판매 (광물이름) (숫자, 전부)'
    commands['시세'] ='광물들의 시세를 볼수 있습니다'
    dir.update( commands )

    # 자원 노드 추가 
    dir = db.reference('자원')
    items = {}
    items['돌'] =  {"가격": 100, "매장량": 100000000000, 'rate':256}
    items['석탄'] = {"가격": 1000, "매장량": 1000000000, 'rate':128}
    items['철'] =  {"가격": 10000, "매장량": 100000000, 'rate':64}
    items['은'] =  {"가격": 20000, "매장량": 50000000, 'rate':32}
    items['금'] = {"가격": 100000, "매장량": 10000000, 'rate':16}
    items['다이아몬드'] = {"가격": 1000000, "매장량": 1000000, 'rate':8}
    items['레드다이아'] = {"가격": 2000000, "매장량": 500000, 'rate':4}
    items['우라늄'] = {"가격": 10000000, "매장량": 1000000, 'rate':2}
    items['비브라늄'] = {"가격": 30000000, "매장량": 1000000, 'rate':1}
    dir.update(items)


# db 초기세팅
migration()
user_init('아토샘#6552')



# db 세팅 체크 
# get_node('명령어')
# get_node('자원')
# show_node('명령어')
# show_node('자원')


def show_node(node_name):
    dir = db.reference(node_name)
    node = dir.get()
    if type(node) == dict:
        for k, v in node.items():
            print(f"{k}: {v}")    
    elif type(node) == list:
        for v in node:
            print(f"v: {v}")

def get_node(node_name):
    dir = db.reference(node_name)
    print("-"*80)
    print(f"type: {type(dir.get())}")
    print("-"*80)