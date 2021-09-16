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
firebase_admin.initialize_app(cred, {'databaseURL': config.firebase_url})

dir = db.reference('test')
dir.update( { 'name' : 'ato' } )
dir.update( { 'age': 29 })
all = dir.get()
show_node(all)
print("-"*80)

dir.set( { 'name': '아토쌤'})

all = dir.get()
show_node(all)


'''
파이어베이스 db 변경, update vs set
- update() : 해당 키의 값만 변경
- set() : 노드 전체를 지우고, 새로운 키와값을 세팅 
'''