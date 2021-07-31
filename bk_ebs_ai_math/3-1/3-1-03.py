# 궁금한 선수의 데이터 검색하기

import pandas as pd

fifa2019 = pd.read_csv('bk_ebs_ai/3-1/fifa2019.csv')

sub1 = fifa2019.loc[14]

print(sub1)
