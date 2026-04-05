import pandas as pd

def load_transaction_data():
    df = pd.read_csv("data/Customer_Intelligence_Revenue_Optimization.csv")
    print("Dataset Loaded Successfully")
    print("Shape:", df.shape)
    return df