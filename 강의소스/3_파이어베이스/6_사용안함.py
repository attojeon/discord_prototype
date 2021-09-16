import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import config 

def show_node(node):
    for k, v in node.items():
        print(f"{k}: {v}")    

cred = credentials.Certificate(config.firebase_secret_file)
firebase_admin.initialize_app(cred, {'databaseURL' : config.firebase_url})


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

show_node(dir.get())

items = []
items.append( {'석탄': 1})
items.append( {'철': 0})
items.append( {'돌': 0})
items.append( {'금': 0})
items.append( {'다이아몬드': 0})
items.append( {'레드다이아': 0})
items.append( {'우라늄': 0})
items.append( {'비브라늄': 0})

# username = '아토샘#6552'
# dir.update({ username : items })
oneuser = {}
oneuser['아토샘'] = items

dir = db.reference('랭킹')
dir.update( oneuser)
show_node( dir.get())