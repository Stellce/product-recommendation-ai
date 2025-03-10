import pandas as pd


def load_data(file_path):
    data = pd.read_excel(file_path)
    return data


def preprocess_data(data):
    data['purchased_at'] = pd.to_datetime(data['purchased_at'], errors='coerce')
    data['is_on_wishlist'] = data['is_on_wishlist'].astype(bool)
    data['is_in_cart'] = data['is_in_cart'].astype(bool)
    data['price'] = data['price'].astype(float)

    data['interaction_score'] = data.apply(calculate_interaction_score, axis=1, current_date=pd.Timestamp.now())

    return data


def calculate_interaction_score(row, current_date):
    score = row['price'] * 0.5

    if row['is_on_wishlist']:
        score += 1  # add weight if in wishlist
    if row['is_in_cart']:
        score += 2  # higher weight if in cart

    days_since_purchase = (current_date - row['purchased_at']).days if pd.notnull(row['purchased_at']) else 0
    recency_score = max(1, 30 - days_since_purchase // 30)
    score += recency_score

    return score
