import data_preparation as dp
import model_training as mt
import pickle

def main():
    # Load and preprocess data
    file_path = input("File path: ")
    if not file_path:
        file_path = 'data.xlsx'
        print(file_path)
    data = dp.load_data(file_path)
    data = dp.preprocess_data(data)


    # Load the trained model
    with open("trained_model.pkl", "rb") as file:
        algo = pickle.load(file)

    # Get recommendations for a specific user
    user_id = input('User ID: ')
    if not user_id:
        user_id = '1'
        print(user_id)
    recommendations = mt.get_recommendations(user_id, data, algo, top_n=5)
    print(f"Recommendations for user {user_id}: {recommendations}")

if __name__ == '__main__':
    while True:
        main()

