# 원하는 범위의 데이터 검색하기

import pandas as pd

fifa2019 = pd.read_csv('bk_ebs_ai/3-1/fifa2019.csv')

# 인덱스 레이블 2부터 16까지인 행 값을 sub2에 저장하기
sub2 = fifa2019.loc[2:16]

print(sub2)
