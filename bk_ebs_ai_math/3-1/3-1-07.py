# 우리나라 선수들 출력하기

import pandas as pd

fifa2019 = pd.read_csv('bk_ebs_ai/3-1/fifa2019.csv')

korea_player = fifa2019['Nationality'] == 'Korea Republic'
print(korea_player)

sub5 = fifa2019.loc[korea_player]
print(sub5)
