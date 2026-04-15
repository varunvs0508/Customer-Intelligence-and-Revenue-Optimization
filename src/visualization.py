import matplotlib.pyplot as plt

def create_dashboard(df, customer_metrics, category_revenue, monthly_sales, discount_return):
    print("\n=== Data Visualization ===")

    plt.figure(figsize=(18, 10))
    colors = {
        "blue": "#4C72B0",
        "green": "#55A868",
        "red": "#C44E52",
        "purple": "#8172B2"
    }

    # Customer Segment Distribution (Horizontal + Labels)
    plt.subplot(2, 3, 1)
    segment_counts = customer_metrics['customer_segment'].value_counts().sort_values()
    ax1 = segment_counts.plot(kind='barh', color=colors["blue"])
    plt.title("Customer Segment Distribution")
    plt.xlabel("Number of Customers")
    plt.ylabel("Customer Segment")

    for i, v in enumerate(segment_counts):
        ax1.text(v, i, f'{v}', va='center')

    # Monthly Sales Trend (Line + Grid)
    plt.subplot(2, 3, 2)
    monthly_sales.plot(marker='o', color=colors["green"])
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Revenue")
    plt.grid(True, linestyle='--', alpha=0.5)

    # Category-wise Revenue (Horizontal + Labels)
    plt.subplot(2, 3, 3)
    cat_rev_sorted = category_revenue.sort_values()
    ax3 = cat_rev_sorted.plot(kind='barh', color=colors["green"])
    plt.title("Category-wise Revenue")
    plt.xlabel("Total Revenue")
    plt.ylabel("Category")

    for i, v in enumerate(cat_rev_sorted):
        ax3.text(v, i, f'{v:,.0f}', va='center')

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
    plt.ylabel("")

    # Return Rate by Category (Horizontal + Labels)
    plt.subplot(2, 3, 5)
    return_sorted = discount_return.sort_values()
    ax5 = return_sorted.plot(kind='barh', color=colors["red"])
    plt.title("Return Rate by Category (%)")
    plt.xlabel("Return Rate (%)")
    plt.ylabel("Category")

    for i, v in enumerate(return_sorted):
        ax5.text(v, i, f'{v:.1f}%', va='center')

    # Customer Spending Distribution (Histogram)
    plt.subplot(2, 3, 6)
    plt.hist(customer_metrics['total_spent'], bins=30, color=colors["purple"], edgecolor='black')
    plt.title("Customer Spending Distribution")
    plt.xlabel("Total Spend")
    plt.ylabel("Number of Customers")
    plt.grid(True, linestyle='--', alpha=0.5)

    # Layout
    plt.tight_layout()
    plt.savefig("shoppulse_customer_analytics.png", dpi=300, bbox_inches='tight')
    plt.show()

    print("Dashboard saved")