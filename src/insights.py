def generate_business_insights(df, customer_metrics):
    print("\n=== Key Business Insights ===")

    total_revenue = df['order_value'].sum()

    top_20_pct = int(0.2 * len(customer_metrics))
    top_revenue = customer_metrics.sort_values(
        by='total_spent', ascending=False
    ).head(top_20_pct)['total_spent'].sum()

    print(f"\nTop 20% customers contribute {round(top_revenue / total_revenue * 100, 2)}% of revenue")

    premium_repeat_rate = customer_metrics[
        customer_metrics['customer_segment'] == 'Premium'
    ]['total_orders'].mean()

    print(f"\nPremium Avg Orders: {premium_repeat_rate:.2f}")

    fashion_returns = df[df['category'] == 'Fashion']['order_status']
    fashion_return_rate = (fashion_returns == 'Returned').mean() * 100

    print(f"\nFashion Return Rate: {fashion_return_rate:.2f}%")