def perform_eda(df, customer_metrics):
    print("\n=== Exploratory Data Analysis ===")

    print("\nAverage Order Value (AOV):", df['order_value'].mean())

    repeat_customers = customer_metrics[customer_metrics['total_orders'] > 1]
    print("Repeat Customers %:", round(len(repeat_customers) / len(customer_metrics) * 100, 2))

    category_revenue = df.groupby('category')['order_value'].sum().sort_values(ascending=False)
    print("\nCategory-wise Revenue:")
    print(category_revenue)

    discount_return = df.groupby('category')['order_status'] \
        .apply(lambda x: (x == 'Returned').mean() * 100)

    print("\nReturn Rate by Category (%):")
    print(discount_return)

    df['Month'] = df['order_date'].dt.month
    monthly_sales = df.groupby('Month')['order_value'].sum()

    return category_revenue, discount_return, monthly_sales