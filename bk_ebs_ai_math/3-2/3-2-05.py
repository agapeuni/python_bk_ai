import pandas as pd

iris = pd.read_csv('bk_ebs_ai/3-2/Iris.csv')

print(iris.head(2))
print(iris.info( ))
print(iris.describe( ))
