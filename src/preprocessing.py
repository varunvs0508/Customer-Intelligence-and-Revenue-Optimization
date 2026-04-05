import pandas as pd
def preprocess_data(df):
    print("\n=== Data Cleaning & Preprocessing ===")

    df['order_date'] = pd.to_datetime(df['order_date'], format="mixed", dayfirst=True)

    df = df[df['order_status'] != 'Cancelled']

    df['discount_pct'] = df['discount_pct'].fillna(0)
    df['payment_mode'] = df['payment_mode'].fillna('Unknown')

    df = df.drop_duplicates()

    Q1 = df['order_value'].quantile(0.25)
    Q3 = df['order_value'].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df['order_value'] >= lower) & (df['order_value'] <= upper)]

    print("Cleaned Records:", len(df))
    return df