# Module 12 Assignment: Business Analytics Fundamentals and Applications
# GreenGrocer Data Analysis

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Welcome message
print("=" * 60)
print("GREENGROCER BUSINESS ANALYTICS")
print("=" * 60)

# ----- USE THE FOLLOWING CODE TO CREATE SAMPLE DATA (DO NOT MODIFY) -----
# Set seed for reproducibility
np.random.seed(42)

# Store information
stores = ["Tampa", "Orlando", "Miami", "Jacksonville", "Gainesville"]
store_data = {
    "Store": stores,
    "SquareFootage": [15000, 12000, 18000, 10000, 8000],
    "StaffCount": [45, 35, 55, 30, 25],
    "YearsOpen": [5, 3, 7, 2, 1],
    "WeeklyMarketingSpend": [2500, 2000, 3000, 1800, 1500]
}

# Create store dataframe
store_df = pd.DataFrame(store_data)

# Product categories and departments
departments = ["Produce", "Dairy", "Bakery", "Grocery", "Prepared Foods"]
categories = {
    "Produce": ["Organic Vegetables", "Organic Fruits", "Fresh Herbs"],
    "Dairy": ["Milk & Cream", "Cheese", "Yogurt"],
    "Bakery": ["Bread", "Pastries", "Cakes"],
    "Grocery": ["Grains", "Canned Goods", "Snacks"],
    "Prepared Foods": ["Hot Bar", "Salad Bar", "Sandwiches"]
}

# Generate sales data for each store
sales_data = []
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

# Base performance factors for each store (relative scale)
store_performance = {
    "Tampa": 1.0, 
    "Orlando": 0.85, 
    "Miami": 1.2, 
    "Jacksonville": 0.75, 
    "Gainesville": 0.65
}

# Base performance factors for each department (relative scale)
dept_performance = {
    "Produce": 1.2,
    "Dairy": 1.0,
    "Bakery": 0.85,
    "Grocery": 0.95,
    "Prepared Foods": 1.1
}

# Generate daily sales data for each store, department, and category
for date in dates:
    # Seasonal factor (higher in summer and December)
    month = date.month
    seasonal_factor = 1.0
    if month in [6, 7, 8]:  # Summer
        seasonal_factor = 1.15
    elif month == 12:  # December
        seasonal_factor = 1.25
    elif month in [1, 2]:  # Winter
        seasonal_factor = 0.9
    
    # Day of week factor (weekends are busier)
    dow_factor = 1.3 if date.dayofweek >= 5 else 1.0  # Weekend vs weekday
    
    for store in stores:
        store_factor = store_performance[store]
        
        for dept in departments:
            dept_factor = dept_performance[dept]
            
            for category in categories[dept]:
                # Base sales amount
                base_sales = np.random.normal(loc=500, scale=100)
                
                # Calculate final sales with all factors and some randomness
                sales_amount = base_sales * store_factor * dept_factor * seasonal_factor * dow_factor
                sales_amount = sales_amount * np.random.normal(loc=1.0, scale=0.1)  # Add noise
                
                # Calculate profit margin (different base margins for departments)
                base_margin = {
                    "Produce": 0.25,
                    "Dairy": 0.22,
                    "Bakery": 0.35,
                    "Grocery": 0.20,
                    "Prepared Foods": 0.40
                }[dept]
                profit_margin = base_margin * np.random.normal(loc=1.0, scale=0.05)
                profit_margin = max(min(profit_margin, 0.5), 0.15)  # Keep within reasonable range
                
                # Calculate profit
                profit = sales_amount * profit_margin
                
                # Add record
                sales_data.append({
                    "Date": date,
                    "Store": store,
                    "Department": dept,
                    "Category": category,
                    "Sales": round(sales_amount, 2),
                    "ProfitMargin": round(profit_margin, 4),
                    "Profit": round(profit, 2)
                })

# Create sales dataframe
sales_df = pd.DataFrame(sales_data)

# Generate customer data
customer_data = []
total_customers = 5000

# Age distribution parameters
age_mean, age_std = 42, 15

# Income distribution parameters (in $1000s)
income_mean, income_std = 85, 30

# Create customer segments (will indirectly influence spending)
segments = ["Health Enthusiast", "Gourmet Cook", "Family Shopper", "Budget Organic", "Occasional Visitor"]
segment_probabilities = [0.25, 0.20, 0.30, 0.15, 0.10]

# Store preference probabilities (matches store performance somewhat)
store_probs = {
    "Tampa": 0.25,
    "Orlando": 0.20,
    "Miami": 0.30,
    "Jacksonville": 0.15,
    "Gainesville": 0.10
}

for i in range(total_customers):
    # Basic demographics
    age = int(np.random.normal(loc=age_mean, scale=age_std))
    age = max(min(age, 85), 18)  # Keep age in reasonable range
    
    gender = np.random.choice(["M", "F"], p=[0.48, 0.52])
    
    income = int(np.random.normal(loc=income_mean, scale=income_std))
    income = max(income, 20)  # Minimum income
    
    # Customer segment
    segment = np.random.choice(segments, p=segment_probabilities)
    
    # Preferred store
    preferred_store = np.random.choice(stores, p=list(store_probs.values()))
    
    # Shopping behavior - influenced by segment
    if segment == "Health Enthusiast":
        visit_frequency = np.random.randint(8, 15)  # Visits per month
        avg_basket = np.random.normal(loc=75, scale=15)
    elif segment == "Gourmet Cook":
        visit_frequency = np.random.randint(4, 10)
        avg_basket = np.random.normal(loc=120, scale=25)
    elif segment == "Family Shopper":
        visit_frequency = np.random.randint(5, 12)
        avg_basket = np.random.normal(loc=150, scale=30)
    elif segment == "Budget Organic":
        visit_frequency = np.random.randint(6, 10)
        avg_basket = np.random.normal(loc=60, scale=10)
    else:  # Occasional Visitor
        visit_frequency = np.random.randint(1, 5)
        avg_basket = np.random.normal(loc=45, scale=15)
    
    # Ensure values are reasonable
    visit_frequency = max(min(visit_frequency, 30), 1)
    avg_basket = max(avg_basket, 15)
    
    # Loyalty tier based on combination of frequency and spending
    monthly_spend = visit_frequency * avg_basket
    if monthly_spend > 1000:
        loyalty_tier = "Platinum"
    elif monthly_spend > 500:
        loyalty_tier = "Gold"
    elif monthly_spend > 200:
        loyalty_tier = "Silver"
    else:
        loyalty_tier = "Bronze"
    
    # Add to customer data
    customer_data.append({
        "CustomerID": f"C{i+1:04d}",
        "Age": age,
        "Gender": gender,
        "Income": income * 1000,  # Convert to actual income
        "Segment": segment,
        "PreferredStore": preferred_store,
        "VisitsPerMonth": visit_frequency,
        "AvgBasketSize": round(avg_basket, 2),
        "MonthlySpend": round(visit_frequency * avg_basket, 2),
        "LoyaltyTier": loyalty_tier
    })

# Create customer dataframe
customer_df = pd.DataFrame(customer_data)

# Create some calculated operational metrics for stores
operational_data = []

for store in stores:
    # Get store details
    store_row = store_df[store_df["Store"] == store].iloc[0]
    square_footage = store_row["SquareFootage"]
    staff_count = store_row["StaffCount"]
    
    # Calculate store metrics
    store_sales = sales_df[sales_df["Store"] == store]["Sales"].sum()
    store_profit = sales_df[sales_df["Store"] == store]["Profit"].sum()
    
    # Calculate derived metrics
    sales_per_sqft = store_sales / square_footage
    profit_per_sqft = store_profit / square_footage
    sales_per_staff = store_sales / staff_count
    inventory_turnover = np.random.uniform(12, 18) * store_performance[store]
    customer_satisfaction = min(5, np.random.normal(loc=4.0, scale=0.3) * 
                                (store_performance[store] ** 0.5))
    
    # Add to operational data
    operational_data.append({
        "Store": store,
        "AnnualSales": round(store_sales, 2),
        "AnnualProfit": round(store_profit, 2),
        "SalesPerSqFt": round(sales_per_sqft, 2),
        "ProfitPerSqFt": round(profit_per_sqft, 2),
        "SalesPerStaff": round(sales_per_staff, 2),
        "InventoryTurnover": round(inventory_turnover, 2),
        "CustomerSatisfaction": round(customer_satisfaction, 2)
    })

# Create operational dataframe
operational_df = pd.DataFrame(operational_data)

# Print data info
print("\nDataframes created successfully. Ready for analysis!")
print(f"Sales data shape: {sales_df.shape}")
print(f"Customer data shape: {customer_df.shape}")
print(f"Store data shape: {store_df.shape}")
print(f"Operational data shape: {operational_df.shape}")

# Print sample of each dataframe
print("\nSales Data Sample:")
print(sales_df.head(3))
print("\nCustomer Data Sample:")
print(customer_df.head(3))
print("\nStore Data Sample:")
print(store_df)
print("\nOperational Data Sample:")
print(operational_df)
# ----- END OF DATA CREATION -----

# TODO 1: Descriptive Analytics - Overview of Current Performance

def analyze_sales_performance():
    total_sales = sales_df["Sales"].sum()
    total_profit = sales_df["Profit"].sum()
    avg_profit_margin = sales_df["ProfitMargin"].mean()
    sales_by_store = sales_df.groupby("Store")["Sales"].sum()
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum()
    return {
        'total_sales': total_sales,
        'total_profit': total_profit,
        'avg_profit_margin': avg_profit_margin,
        'sales_by_store': sales_by_store,
        'sales_by_dept': sales_by_dept
    }


def visualize_sales_distribution():
    store_fig = plt.figure()
    sales_df.groupby("Store")["Sales"].sum().plot(kind="bar", title="Sales by Store")
    dept_fig = plt.figure()
    sales_df.groupby("Department")["Sales"].sum().plot(kind="bar", title="Sales by Department")
    time_fig = plt.figure()
    sales_df.groupby(sales_df["Date"].dt.month)["Sales"].sum().plot(title="Monthly Sales")
    return store_fig, dept_fig, time_fig


def analyze_customer_segments():
    segment_counts = customer_df["Segment"].value_counts()
    segment_avg_spend = customer_df.groupby("Segment")["MonthlySpend"].mean()
    segment_loyalty = pd.crosstab(customer_df["Segment"], customer_df["LoyaltyTier"])
    return {
        'segment_counts': segment_counts,
        'segment_avg_spend': segment_avg_spend,
        'segment_loyalty': segment_loyalty
    }


# TODO 2: Diagnostic Analytics

def analyze_sales_correlations():
    merged = operational_df.merge(store_df, on="Store")
    store_correlations = merged.corr(numeric_only=True)
    top_correlations = list(store_correlations["AnnualSales"].sort_values(ascending=False).items())[:5]
    correlation_fig = plt.figure()
    store_correlations["AnnualSales"].sort_values().plot(kind="barh", title="Sales Correlations")
    return {
        'store_correlations': store_correlations,
        'top_correlations': top_correlations,
        'correlation_fig': correlation_fig
    }


def compare_store_performance():
    efficiency_metrics = operational_df[["Store","SalesPerSqFt","SalesPerStaff"]]
    performance_ranking = operational_df.set_index("Store")["AnnualProfit"].sort_values(ascending=False)
    comparison_fig = plt.figure()
    performance_ranking.plot(kind="bar", title="Store Profit Ranking")
    return {
        'efficiency_metrics': efficiency_metrics,
        'performance_ranking': performance_ranking,
        'comparison_fig': comparison_fig
    }


def analyze_seasonal_patterns():
    monthly_sales = sales_df.groupby(sales_df["Date"].dt.month)["Sales"].sum()
    dow_sales = sales_df.groupby(sales_df["Date"].dt.dayofweek)["Sales"].sum()
    seasonal_fig = plt.figure()
    monthly_sales.plot(title="Seasonal Sales")
    return {
        'monthly_sales': monthly_sales,
        'dow_sales': dow_sales,
        'seasonal_fig': seasonal_fig
    }


# TODO 3: Predictive Analytics

def predict_store_sales():
    merged = operational_df.merge(store_df, on="Store")
    x = merged["SquareFootage"]
    y = merged["AnnualSales"]
    slope, intercept, r, p, se = stats.linregress(x, y)
    predictions = intercept + slope * x
    model_fig = plt.figure()
    plt.scatter(x, y)
    plt.plot(x, predictions)
    plt.title("Sales Prediction Model")
    return {
        'coefficients': {"SquareFootage": slope},
        'r_squared': r**2,
        'predictions': predictions,
        'model_fig': model_fig
    }


def forecast_department_sales():
    dept_trends = sales_df.groupby([sales_df["Date"].dt.month,"Department"])["Sales"].sum().unstack()
    growth_rates = dept_trends.pct_change().mean()
    forecast_fig = plt.figure()
    dept_trends.plot()
    return {
        'dept_trends': dept_trends,
        'growth_rates': growth_rates,
        'forecast_fig': forecast_fig
    }


# TODO 4: Integrated Analysis

def identify_profit_opportunities():
    grouped = sales_df.groupby(["Store","Department"])["Profit"].sum()
    top_combinations = grouped.sort_values(ascending=False).head(10)
    underperforming = grouped.sort_values().head(10)
    opportunity_score = operational_df.set_index("Store")["AnnualProfit"]
    return {
        'top_combinations': top_combinations,
        'underperforming': underperforming,
        'opportunity_score': opportunity_score
    }


def develop_recommendations():
    return [
        "Increase marketing in high performing stores",
        "Expand prepared foods department",
        "Optimize staffing levels",
        "Target high value customers",
        "Adjust inventory for seasonal demand"
    ]


# TODO 5: Executive Summary

def generate_executive_summary():
    print("Overview:\nGreenGrocer data analysis evaluated sales, customers, and store operations.")
    print("\nKey Findings:")
    print("- Miami highest sales")
    print("- Prepared foods highest profit")
    print("- Weekends busiest")
    print("\nRecommendations:")
    print("- Increase marketing")
    print("- Expand high margin departments")
    print("- Improve staffing efficiency")
    print("\nExpected Impact:\nImproved profitability and operational efficiency.")
