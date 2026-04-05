def build_customer_metrics(df):
    print("\n=== Feature Engineering ===")

    customer_metrics = df.groupby('customer_id').agg(
        total_orders=('order_id', 'count'),
        total_spent=('order_value', 'sum'),
        avg_order_value=('order_value', 'mean'),
        avg_discount=('discount_pct', 'mean'),
        return_rate=('order_status', lambda x: (x == 'Returned').mean())
    ).reset_index()

    def segment(row):
        if row['total_spent'] > customer_metrics['total_spent'].quantile(0.8):
            return 'Premium'
        elif row['total_spent'] > customer_metrics['total_spent'].quantile(0.4):
            return 'Regular'
        else:
            return 'Low-Value'

    customer_metrics['customer_segment'] = customer_metrics.apply(segment, axis=1)

    print("Customer Metrics Generated")
    return customer_metrics