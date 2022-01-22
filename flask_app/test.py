""" import pickle

with open('model/fraud_model.bin', 'rb') as f_in:
    model2 = pickle.load(f_in)

prediction = model2.predict([[3, 14650.1, 908817173, 19373.0, 4722.9, 0.0, 0.0,]])

print(prediction[0]) """

import pandas as pd

df1 = pd.read_csv("model\\fraud_data1_1_1.csv")
df2 = pd.read_csv("model\\fraud_data1_1_2.csv")
df3 = pd.read_csv("model\\fraud_data2.csv")

df = pd.concat([df1,df2,df3])
print(df.head())