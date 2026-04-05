from src.data_loader import load_transaction_data
from src.preprocessing import preprocess_data
from src.feature_engineering import build_customer_metrics
from src.eda import perform_eda
from src.database import load_to_db
from src.insights import generate_business_insights
from src.visualization import create_dashboard

def main():
    print("ShopPulse Customer Intelligence & Revenue Optimization")
    print("=" * 60)

    df = load_transaction_data()
    df = preprocess_data(df)

    customer_metrics = build_customer_metrics(df)

    category_revenue, discount_return, monthly_sales = perform_eda(df, customer_metrics)

    load_to_db(df)
    generate_business_insights(df, customer_metrics)

    create_dashboard(df, customer_metrics, category_revenue, monthly_sales, discount_return)

    print("\n=== Project Completed Successfully ===")

if __name__ == "__main__":
    main()