import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import config 

cred = credentials.Certificate(config.firebase_secret_file)
firebase_admin.initialize_app(cred, {'databaseURL' : config.firebase_url})
dir = db.reference('리스트테스트')


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


def reset_test():
    dir.set('')  # 리스트 지우기 

'''
list 형을 ref.set()하면 전체를 새로 작성하게 됨. 
- 0~ indexed id가 생성됨 
'''
def append_test():
    items = []
    items.append({'ato': {"철": 0}})
    items.append({"zeus": {"석탄": 0}})
    items.append({'atto': {"철": 0}})
    items.append({"yoon": {"석탄": 0}})
    dir.set(items)

# dir.set(["ato", "zeus", "yoon"])  # => 가능함
# dir.update(["ato", "zeus", "yoon"])  # => 불가능함
### 결론 : 리스트형은 set 가능, update 불가능 

'''
ref.push() 는 uuid id가 발생함. 
'''
def push_test():
    dir.push({'ato': {"철": 0}})
    dir.push({"zeus": {"석탄": 0}})
    # dir.push(["atto", "atojeon"])  => child node list 가 다시 생김 


def remove(node_idx):
    dir

reset_test()
append_test()
# push_test()

show_node( dir.get() )
