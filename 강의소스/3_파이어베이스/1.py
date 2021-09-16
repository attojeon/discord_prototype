import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import config 

def show_node(node):
    print("*"*80)
    print(f"node type: {type(node)}")
    if type(node) == dict:
        for k, v in node.items():
            print(f"{k}: {v}")    
    elif type(node) == list:
        for v in node:
            print(f"v: {v}")
    print("*"*80)   

cred = credentials.Certificate(config.firebase_secret_file)
firebase_admin.initialize_app(cred, {'databaseURL' : config.firebase_url})

dir = db.reference('명령어')
dir.update( { '회원가입' : '회원가입 명령어로 데이터베이스에 데이터를 저장'})
dir.update( { 'version': 0.1 })
all = dir.get()

show_node(all)

'''
파이어베이스 db 연결하기
- 가입하기 
- 연결설정하기 
- 간단히 작성하기 
- 딕셔너리 사용법 
''' 