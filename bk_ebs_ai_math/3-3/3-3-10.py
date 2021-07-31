# 데이터를 학습, 평가 데이터로 분리하기

# 데이터 준비하기
import pandas as pd               # 모듈 추가하기
df = pd.read_csv('bk_ebs_ai/3-3/temp_ice.csv', encoding='euc-kr')

print(df.head(5))
