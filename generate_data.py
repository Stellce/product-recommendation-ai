import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parameters for synthetic data
num_customers = 50  # Number of unique customers
num_products = 20   # Number of unique products
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 10, 1)

# Helper function to generate random purchase dates monthly
def generate_monthly_purchases(start, end, probability=0.8):
    dates = pd.date_range(start, end, freq='MS')
    return [date for date in dates if np.random.rand() < probability]

# Generate the dataset
data = []
products_prices = {}
for product_id in range(1, num_products + 1):
    if product_id not in products_prices.keys():
        products_prices[product_id] = np.random.randint(10, 500)

for customer_id in range(1, num_customers + 1):
    for product_id in range(1, num_products + 1):
        # Determine if this customer has a "habit" of buying this product monthly
        if np.random.rand() < 0.3:  # 30% chance of a regular purchase habit
            purchase_dates = generate_monthly_purchases(start_date, end_date)
        else:
            purchase_dates = np.random.choice(pd.date_range(start_date, end_date, freq='ME'),
                                              size=np.random.randint(1, 3), replace=False)

        # Add purchases to the data
        for purchase_date in purchase_dates:
            data.append({
                'customer_id': customer_id,
                'product_id': product_id,
                'is_on_wishlist': np.random.choice([True, False]),
                'is_in_cart': np.random.choice([True, False]),
                'purchased_at': purchase_date,
                'price': products_prices[product_id]
            })

df = pd.DataFrame(data)

# Add missing months for customers who skipped a purchase (for testing the AI)
for customer_id in range(1, num_customers + 1):
    skipped_product_id = np.random.randint(1, num_products + 1)
    skip_date = pd.Timestamp(end_date) - timedelta(days=30)  # Skip recent month
    if not ((df['customer_id'] == customer_id) & (df['product_id'] == skipped_product_id) & (df['purchased_at'] == skip_date)).any():
        new_row = pd.DataFrame([{
            'customer_id': customer_id,
            'product_id': skipped_product_id,
            'is_on_wishlist': False,
            'is_in_cart': False,
            'purchased_at': pd.NaT,
            'price': products_prices[skipped_product_id]
        }])
        df = pd.concat([df, new_row], ignore_index=True)

# Sort data for easier inspection
df = df.sort_values(by=['customer_id', 'product_id', 'purchased_at'])

# Save to Excel file
df.to_excel("synthetic_purchase_data.xlsx", index=False)
print("Data generated and saved to synthetic_purchase_data.xlsx")
