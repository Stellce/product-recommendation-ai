# AI-Based Product Recommendation System

## Overview
This project implements an AI-powered product recommendation system using customer purchase data. The system analyzes user behavior, including wishlist additions, cart interactions, and past purchases, to suggest the most relevant products. It leverages machine learning techniques, specifically Singular Value Decomposition (SVD), to generate personalized recommendations.

## Features
- **Data Generation**: Creates synthetic purchase history for testing.
- **Data Preprocessing**: Cleans and transforms raw data into a structured format.
- **Model Training**: Uses SVD for collaborative filtering-based recommendations.
- **Product Recommendation**: Provides personalized product suggestions based on user interaction scores.

## Project Structure
```
├── data_preparation.py    # Loads and preprocesses input data
├── generate_data.py       # Generates synthetic purchase data
├── main.py                # Loads data, runs the model, and provides recommendations
├── model_training.py      # Trains and evaluates the recommendation model
├── train_model.py         # Trains the model and saves it for later use
├── synthetic_purchase_data.xlsx  # Example dataset
└── trained_model.pkl      # Serialized trained model
```

## Installation
### Requirements
Ensure you have Python installed along with the necessary dependencies:
```bash
pip install pandas numpy surprise openpyxl
```

## Usage
### 1. Generate Synthetic Data
Run the following command to create an example dataset:
```bash
python generate_data.py
```
This will generate `synthetic_purchase_data.xlsx`.

### 2. Train the Model
Train the recommendation model using:
```bash
python train_model.py
```
This will save the trained model as `trained_model.pkl`.

### 3. Get Recommendations
Run the main script to obtain product recommendations for a specific user:
```bash
python main.py
```
You will be prompted to enter a file path (default: `data.xlsx`) and a user ID.

## How It Works
1. **Data Generation**
   - `generate_data.py` creates synthetic customer-product interactions, including wishlist status, cart status, and purchase history.
   - It simulates periodic purchases and missing purchase data to test the recommendation system.
2. **Data Preparation**
   - `data_preparation.py` loads and cleans the dataset.
   - Computes an `interaction_score` based on recency, price, and cart/wishlist interactions.
3. **Model Training**
   - `model_training.py` trains an SVD-based collaborative filtering model using Surprise.
   - Splits data into training and test sets, evaluates performance using RMSE.
4. **Recommendations**
   - `main.py` loads the trained model and generates top-N recommendations for a user.

## Future Improvements
- Implement a web API for real-time recommendations.
- Enhance the recommendation algorithm with deep learning techniques.
- Expand feature engineering for better personalization.
