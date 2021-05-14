'''
# 참조 문서: https://www.data.go.kr/iim/api/selectAPIAcountView.do 
#   - 제공상세문서의 각종 코드 값을 반드시 참조해야 함. 
'''

import json
import pprint
import requests
from datetime import datetime 
from urllib.parse import urlencode

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
service_key = 'jEN2Laz4w112BMQec2i/j147DpKIiOI2sbkVDa/d2o1UjrTlybQlSLdVZ9nezp+lUjzg/QnOHzIGzEvEXDi6eQ=='

geo_list = None 
nx = 0
ny = 0
basedate = None 
basetime = None 

weathers_meta = {
    "POP": "강수확률",
    "PTY": "강수형태",
    "R06": "6시간 강수량",
    "REH": "습도",
    "S06": "6시간 신적설",
    "SKY": "하늘상태",
    "T3H": "3시간 기온",
    "TMN": "아침 최저기온",
    "TMX": "낮 최저기온",
    "UUU": "풍속(동서성분)",
    "VVV": "풍속(남북성분)",
    "WAV": "파고",
    "VEC": "풍향",
    "WSD": "풍속",
}

def query():
    #query = "서울특별시 동작구"
    return input("동네예보! 지역을 입력하세요. 예) 서울특별시 동작구 >>> ")

def setup_geo( filename, step=2):
    global geo_list 
    file = open(filename, "rt", encoding="utf-8")
    geo_json = json.load(file)
    file.close()
    geo_list = list(geo_json)
    print(len(geo_list))

def get_coord(address):
    # error check
    if address and len(address.split(' ')) == 2:
        sido, gu = address.split(" ")
        for loc in geo_list:
            if loc[0] == sido and loc[1] == gu:
                return (loc[3], loc[4])
        return None
    else:
        return None

def get_basedate():
    return datetime.now().strftime('%Y%m%d')


#########################################################
# 문서에 의하면: 현재시간 직전 발표시간의 자료를 갖고와야 함.
#########################################################
def get_basetime(): 
    times = ['0200', '0500', '0800', '1100', '1400', '1700', '2000', '2300'] 
    hour = datetime.now().strftime('%H00') 
    for idx, t in enumerate( times): 
        if t >= hour and idx>0:
            return times[idx-1] 
        elif t>=hour and idx == 0: 
            return times[0] 
        elif t>=hour and idx == len(times)-1 :
            return times[len(times)-1]
    return times[0]
    
#########################################################
# 동네예보를 위해 필요한 변수 세팅
# nx, ny, basedate, basetime 
#########################################################
def setup_info(q = '서울특별시 동작구'):
    global nx, ny, basedate, basetime 
    # q = query()
    nxy = get_coord(q)
    if nxy:
        nx, ny = nxy
        basedate = get_basedate()
        basetime = get_basetime()
        # basetime = '1100'
        print(f"nx: {nx}, ny: {ny}, basedate:{basedate}, basetime: {basetime}") 
    else:
        print("주소 입력 양식이 맞지 않습니다. 예)서울특별시 동작구")


def show_weather(weather_infos):
    meta_keys = weathers_meta.keys()
    ret = ''
    for k in meta_keys:
        for w in weather_infos:
            if w['category'] == k:
                meta_name = weathers_meta[k]
                the_date = w['fcstDate']
                the_time = w['fcstTime']
                val = w['fcstValue']
                print(f"{meta_name}: {the_date}, {the_time}, 예상값: {val}")
                ret += f"{meta_name}: {the_date}, {the_time}, 예상값: {val}\n"

    return ret 

# main 
def predict_weather(q_loc):
    setup_geo("./open_geo.json", 2)
    setup_info(q_loc)

    params = {
        'ServiceKey': service_key,
        'pageNo': '1',
        'numOfRows': '10', 
        'dataType': 'json',
        'base_date': basedate,      # 20210511
        'base_time': basetime,      # 1700
        'nx': nx,                   # 59
        'ny': ny                    # 125
    }
    encoded = urlencode(params).encode()
    response = requests.get(url, encoded)


    if response.status_code == 200:
        json_obj = response.json()
        weather_infos = json_obj['response']['body']['items']['item']
        # pprint.pprint(weather_infos)

        return show_weather(weather_infos)
    else:
        return "수행 중 에러 발생..."

def main():
    q = input("지역 입력>>> ")
    predict_weather(q) 

if __name__ == "__main__":
    main()