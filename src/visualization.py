import matplotlib.pyplot as plt

def create_dashboard(df, customer_metrics, category_revenue, monthly_sales, discount_return):
    print("\n=== Data Visualization ===")

    plt.figure(figsize=(18, 10))

    plt.subplot(2, 3, 1)
    customer_metrics['customer_segment'].value_counts().plot(kind='bar', color='skyblue')
    plt.title("Customer Segment Distribution")

    plt.subplot(2, 3, 2)
    monthly_sales.plot(marker='o')
    plt.title("Monthly Sales Trend")

    plt.subplot(2, 3, 3)
    category_revenue.plot(kind='bar', color='lightgreen')
    plt.title("Category-wise Revenue")
    plt.xticks(rotation=45)

    plt.subplot(2, 3, 4)
    df['order_status'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Order Status Distribution")

    plt.subplot(2, 3, 5)
    discount_return.plot(kind='bar', color='orange')
    plt.title("Return Rate by Category (%)")
    plt.xticks(rotation=45)

    plt.subplot(2, 3, 6)
    plt.axis('off')

    plt.tight_layout()
    plt.savefig("shoppulse_customer_analytics.png", dpi=300)
    plt.show()

    print("Dashboard saved")