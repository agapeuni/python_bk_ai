# 여러 행의 데이터 중 원하는 열 값만 골라 출력하기

import pandas as pd

fifa2019 = pd.read_csv('bk_ebs_ai/3-1/fifa2019.csv')

# 0~9행, 1, 2열값을 sub4에 저장하기
sub4 = fifa2019.iloc[0:10, 1:3]

print(sub4)
