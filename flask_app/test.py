import pickle

with open('model/fraud_model.bin', 'rb') as f_in:
    model2 = pickle.load(f_in)

prediction = model2.predict([[3, 14650.1, 908817173, 19373.0, 4722.9, 0.0, 0.0,]])

print(prediction[0])