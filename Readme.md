# 🧠 Customer Intelligence & Revenue Optimization System

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pandas](https://img.shields.io/badge/Data-Pandas-orange)
![MySQL](https://img.shields.io/badge/Database-MySQL-blue)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📌 Overview

It is an **end-to-end customer intelligence and retail analytics system** designed to analyze transactional data and generate **actionable business insights**.

This project simulates a real-world analytics pipeline used by retail companies to:

* Understand customer behavior 🧠
* Segment customers based on value 💎
* Optimize revenue strategies 💰
* Monitor sales performance 📈

---

## 🎯 Key Objectives

* Perform end-to-end data analysis on retail transactions
* Build customer-level metrics (RFM-style insights)
* Segment customers into Premium, Regular, and Low-Value
* Analyze revenue trends across categories and time
* Evaluate the impact of discounts on returns
* Generate business-ready insights

---

## 🏗️ Project Architecture

```text
Data → Preprocessing → Feature Engineering → EDA → Visualization → Database → Insights
```

---

## 📂 Project Structure

```text
shoppulse-customer-intelligence/
│
├── data/
│   └── Customer_Intelligence_Revenue_Optimization.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── eda.py
│   ├── visualization.py
│   ├── database.py
│   └── insights.py
│
├── shoppulse_customer_analytics.png
├── main.py
├── requirements.txt
├── README.md
├── .env (ignored)
└── .gitignore
```

---

## ⚙️ Features

✔️ Data Cleaning & Preprocessing (missing values, duplicates, outliers)

✔️ Customer Feature Engineering
→ Total Spend, AOV, Return Rate, Order Frequency

✔️ Customer Segmentation
→ Premium | Regular | Low-Value

✔️ Exploratory Data Analysis (EDA)

✔️ Advanced Visualization Dashboard

✔️ MySQL Database Integration (via SQLAlchemy)

✔️ Secure Configuration using `.env`

✔️ Business Insights Generation

---

## 📊 Dashboard

![ShopPulse Dashboard](shoppulse_customer_analytics.png)

### 🔍 Key Observations:

* 📌 Customer spending is highly skewed (few high-value customers)
* 📌 Premium customers contribute a major share of revenue
* 📌 Certain categories drive most of the sales
* 📌 Higher discounts are associated with increased return rates
* 📌 Monthly sales trends reveal seasonal patterns

---

## 🛠️ Tech Stack

| Category       | Tools Used    |
| -------------- | ------------- |
| Language       | Python        |
| Data Analysis  | Pandas        |
| Visualization  | Matplotlib    |
| Database       | MySQL         |
| ORM            | SQLAlchemy    |
| Env Management | python-dotenv |

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
DB_CONNECTION=mysql+mysqlconnector://username:password@localhost/dataanalysisproject
```

> ⚠️ This file is excluded using `.gitignore` for security.

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/shoppulse-customer-intelligence.git
cd shoppulse-customer-intelligence
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Add Dataset

Place your dataset inside:

```text
data/Customer_Intelligence_Revenue_Optimization.csv
```

---

### 4️⃣ Configure Environment

Create `.env` file and add your database credentials

---

### 5️⃣ Run Project

```bash
python main.py
```

---

## 📈 Output

* 📊 Customer Analytics Dashboard
* 📉 Category & Revenue Trends
* 🧠 Customer Segmentation Insights
* 🗄️ Data stored in MySQL (optional)

---

## 🔍 Key Business Insights

* Top 20% of customers contribute a significant portion of total revenue (Pareto Principle)
* Premium customers show higher repeat purchase behavior
* Discount-heavy categories tend to have higher return rates
* Customer segmentation enables targeted marketing strategies
* Revenue is concentrated among a few high-performing categories

---

## 📬 Connect With Me

<p align="center">
  <a href="https://www.linkedin.com/in/varun-sai-kedarisetty-bb86bb23b/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Visit%20Profile-blue?style=for-the-badge&logo=linkedin" />
  </a>
</p>

---
