# 전체 선수들의 이름과 선호하는 발 정보 출력하기

import pandas as pd

fifa2019 = pd.read_csv('bk_ebs_ai/3-1/fifa2019.csv')

sub3 = fifa2019.loc[:, ['Name', 'Preferred Foot']]
print(sub3)

sub3 = fifa2019.loc[:, ['Age', 'Name']]
print(sub3)
