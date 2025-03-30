import pandas as pd
import numpy as np
import pickle as pk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# making a data frame
df = pd.read_csv("house_prices.csv")

print(df.columns)
#Index(['LotArea', 'YearBuilt', 'FullBath', 'BedroomAbvGr', 'GarageCars',
#      'SalePrice']     dtype='object')

# make the x and y for storing the train and test data 
x = df.drop(columns="SalePrice")
y = df['SalePrice']


# appling train test split 
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=40)

# Model training 
model = LinearRegression() #Define the model 
model.fit(x_train,y_train) # fit the data 

# Save model 

pk.dump(model,open('model.pkl','wb'))

print("Success! ")






