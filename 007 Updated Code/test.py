import pandas as pd
from datetime import datetime, timedelta

# 주어진 데이터
data = [
    {"name": "jy", "time": datetime.strptime("2023-08-07 17:46:02", "%Y-%m-%d %H:%M:%S"), "text": "안녕하세요"},
    {"name": "jy", "time": datetime.strptime("2023-08-07 17:47:02", "%Y-%m-%d %H:%M:%S"), "text": "안녕하세요"},
    {"name": "sy", "time": datetime.strptime("2023-08-07 17:47:02", "%Y-%m-%d %H:%M:%S"), "text": "안녕하세요"},
    {"name": "sy", "time": datetime.strptime("2023-08-08 17:46:02", "%Y-%m-%d %H:%M:%S"), "text": "집가고싶다"},
]

# 데이터를 DataFrame으로 변환
df = pd.DataFrame(data)

# 이전 텍스트와의 시간 차이가 10초 이내라면 이전 행의 timeblock 값을 사용

block_size = 10  # 10초 기준 시간 블록 크기
check_row = None
df['timeblock'] = None

for index, row in df.iterrows():
    if index < 1 :
        df.loc[index, 'timeblock'] = 0
        row['timeblock'] = 0
        check_row = row
        continue
    
    if (row['time'] - check_row['time']).total_seconds() < 600 :
        df.loc[index,'timeblock'] = check_row['timeblock']
        row['timeblock'] = check_row['timeblock']
    else :
        df.loc[index, 'timeblock'] = check_row['timeblock'] + 1
        row['timeblock'] = check_row['timeblock'] + 1
    check_row = row

print(df)
