import pandas as pd
# data = pd.read_csv('../datasets/titanic/titanic3.csv')
# data.head()

mainpath = r'/Users/lgutierrez/Documents/Desarrollo/python-ml-course/datasets'
filename = r'/titanic/titanic3.csv'
fullpath = mainpath+filename
data = pd.read_csv(fullpath)
data.head()



