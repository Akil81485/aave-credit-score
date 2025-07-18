from src.load_data import load_transactions
from src.feature_engineering import extract_wallet_features
import pandas as pd

if __name__ == "__main__":
    df = load_transactions("data/user_transactions.json")
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    print("Unique Wallets:", df['userWallet'].nunique())
    print("Actions distribution:")
    print(df['action'].value_counts())

    features_df = extract_wallet_features(df)
    print("\nWallet features sample:")
    print(features_df.head())
