import data_preparation as dp
import model_training as mt
import pickle

file_path = "synthetic_purchase_data.xlsx"
data = dp.load_data(file_path)
data = dp.preprocess_data(data)

algo = mt.train_model(data)

with open("trained_model.pkl", "wb") as file:
    pickle.dump(algo, file)

print("Model trained and saved as model.pkl")
