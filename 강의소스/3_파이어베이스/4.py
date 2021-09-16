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

ato = db.reference('test/ato/name')

# 노트의 값 읽기 
print( ato.get() )


'''
파이어베이스 db 값 읽기
- 
'''