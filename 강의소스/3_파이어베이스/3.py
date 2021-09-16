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
# 노트 전체 지우기 
dir.set('')

dir.update( { 'ato/name' : '아토쌤' } )
dir.update( { 'ato/age': 29 })
show_node(dir.get())
print('-'*80)

dir.update( { 'zeus/name' : '제우스쌤' } )
dir.update( { 'zeus/age': 20 })
show_node(dir.get())

dir = db.reference('리스트테스트')
item = []
item.append("ato")
item.append("zeus")
dir.set( item )

# dir.set(["ato", "zeus", "yoon"])  # => 가능함
# dir.update(["ato", "zeus", "yoon"])  # => 불가능함
### 결론 : 리스트형은 set 가능, update 불가능 



'''
파이어베이스 db 변경, 여러 단계의 노드를 한 번에 해결
- update() : '이름1/이름2/이름3 ... 
'''