import matplotlib.pyplot as plt

def create_dashboard(df, customer_metrics, category_revenue, monthly_sales, discount_return):
    print("\n=== Data Visualization ===")

    plt.figure(figsize=(18, 10))

    # 🎨 Color palette
    colors = {
        "blue": "#4C72B0",
        "green": "#55A868",
        "red": "#C44E52",
        "purple": "#8172B2",
        "orange": "#CCB974"
    }

    # Customer Segment Distribution
    plt.subplot(2, 3, 1)
    customer_metrics['customer_segment'].value_counts() \
        .plot(kind='bar', color=colors["blue"])
    plt.title("Customer Segment Distribution")
    plt.xlabel("Customer Segment")
    plt.ylabel("Number of Customers")

    # Monthly Sales Trend
    plt.subplot(2, 3, 2)
    monthly_sales.plot(marker='o', color=colors["green"])
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Revenue")
    plt.grid(True, linestyle='--', alpha=0.5)

    # Category-wise Revenue
    plt.subplot(2, 3, 3)
    category_revenue.plot(kind='bar', color=colors["green"])
    plt.title("Category-wise Revenue")
    plt.xlabel("Category")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)

    # Order Status Distribution (Improved Pie)
    plt.subplot(2, 3, 4)
    df['order_status'].value_counts().plot(
        kind='pie',
        autopct='%1.1f%%',
        colors=[colors["blue"], colors["red"]],
        startangle=90,
        wedgeprops={'edgecolor': 'black'}
    )
    plt.title("Order Status Distribution")
    plt.ylabel("")  # remove default label
    

    # Return Rate by Category
    plt.subplot(2, 3, 5)
    discount_return.plot(kind='bar', color=colors["red"])
    plt.title("Return Rate by Category (%)")
    plt.xlabel("Category")
    plt.ylabel("Return Rate (%)")
    plt.xticks(rotation=45)

    # Customer Spending Distribution (Histogram)
    plt.subplot(2, 3, 6)
    plt.hist(customer_metrics['total_spent'], bins=30,color=colors["purple"], edgecolor='black')
    plt.title("Customer Spending Distribution")
    plt.xlabel("Total Spend")
    plt.ylabel("Number of Customers")
    plt.grid(True, linestyle='--', alpha=0.5)

    # Layout
    plt.tight_layout()
    plt.savefig("shoppulse_customer_analytics.png", dpi=300)
    plt.show()

    print("Dashboard saved")