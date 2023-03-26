import pandas as pd
data = pd.read_csv('insurance.csv')
data.head(5)

data['sex']=data['sex'].replace('female',1)
data['sex']=data['sex'].replace('male',0)

data['smoker'] = data['smoker'].replace('yes',1)
data['smoker'] = data['smoker'].replace('no',0)

data['region'] = data['region'].replace('northwest',0)
data['region'] = data['region'].replace('northeast',1)
data['region'] = data['region'].replace('southwest',2)
data['region'] = data['region'].replace('southeast',3)

x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x,y)

#print( regression.predict([[19,1,27.9,0,1,3]]))










