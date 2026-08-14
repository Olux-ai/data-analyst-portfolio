# SuperStore Sales Analysis Dashboard

## 📊 Project Overview

This project analyzes retail sales data to identify the regions, product categories, and months that are driving profit — and the areas where the business is losing money.

The project follows an end-to-end data analysis process, starting with data cleaning and transformation in **Power Query**, followed by analysis using **Excel PivotTables, PivotCharts, and Slicers**.

The goal is to turn raw sales data into clear business insights that can support better decisions around products, regions, pricing, and profitability.

---

## 🔴 Business Problem

A retail manager wants to know which **regions, categories, and months are driving profit — and where the business is losing money**.

Although the business has detailed transaction data, the raw data does not immediately show which areas are performing well or poorly.

This analysis aims to answer the following questions:

- Which regions generate the highest profit?
- Which product categories are most profitable?
- Which months generate the highest and lowest profit?
- Which products are generating losses?
- Does higher sales always result in higher profit?
- Which areas should management focus on to improve profitability?

---

## 🎯 Objectives

1. Analyze overall sales and profitability.
2. Compare profit performance across regions.
3. Identify the most and least profitable product categories.
4. Analyze monthly profit trends.
5. Identify products generating negative profit.
6. Examine the relationship between sales, quantity, discount, and profit.
7. Build an interactive Excel dashboard.
8. Provide data-driven recommendations for improving profitability.

---

## 📁 Dataset

The dataset contains **9,995 retail sales records** with information about orders, products, customers, regions, sales, discounts, and profit.

### Key Variables

| Column | Description |
|---|---|
| Order Date | Date the order was placed |
| Region | Geographic region of the sale |
| Category | Main product category |
| Sub-Category | Specific product group |
| Product Name | Product sold |
| Sales | Revenue generated |
| Quantity | Number of units sold |
| Discount | Discount applied to the sale |
| Profit | Profit generated from the transaction |
| Year | Year extracted from the order date |
| Month | Month extracted from the order date |
| Year-Month | Combined year and month for trend analysis |
| Profit Margin | Profit relative to sales |
| Revenue Per Unit | Revenue generated per unit sold |

---

## 🧹 Data Cleaning & Preparation

The raw dataset was cleaned and transformed using **Microsoft Power Query**. The preparation process included:

- Reviewing the dataset for inconsistencies
- Correcting data types
- Cleaning and standardizing data
- Preparing date fields for analysis
- Creating additional analytical columns
- Preparing the dataset for PivotTables and visualizations
- Using a customer lookup table and merging queries where required

**Why Power Query?** It made the cleaning process more efficient and repeatable compared with manually editing individual records.

---

## 🔎 Analysis Method

The analysis followed this workflow:

**Raw Data → Data Cleaning → Data Transformation → PivotTable Analysis → Visualization → Insights → Recommendations**

### PivotTable Analysis

PivotTables were used to analyze:

- Profit by Region
- Profit by Category
- Profit by Month
- Profit by Year
- Profit by Product
- Sales by Region
- Sales by Category
- Category and Region performance

### Data Visualization

PivotCharts were created to communicate the findings visually. Slicers were also used to allow the dashboard to be filtered interactively.

---

## 📈 Key Insights

### 1. Regional Profitability

| Region | Profit |
|---|---:|
| West | $108,418.45 |
| East | $91,522.78 |
| South | $46,749.43 |
| Central | $39,706.36 |

**Finding:** The **West region generated the highest profit**, while the **Central region generated the lowest profit** among the four regions. This indicates that profitability varies considerably across regions and that regional performance should be investigated individually.

### 2. Category Profitability

| Category | Sales | Profit |
|---|---:|---:|
| Furniture | $741,999.80 | $18,451.27 |
| Office Supplies | $719,047.03 | $122,490.80 |
| Technology | $836,154.03 | $145,454.95 |

**Finding:** **Technology generated the highest profit**, followed by Office Supplies. Furniture generated significant sales but comparatively low profit. This demonstrates that:

> **High sales do not necessarily mean high profitability.**

Management should therefore evaluate both sales and profit when assessing category performance.

### 3. Loss-Making Products

The analysis identified several products generating negative profit, including:

- Cubify CubeX 3D Printer Double Head Print
- Lexmark MX611dhe Monochrome Laser Printer
- Cubify CubeX 3D Printer Triple Head Print
- Chromcraft Bull-Nose Wood Oval Conference Tables & Bases
- Bush Advantage Collection Racetrack Conference Table

These products require further investigation to understand whether pricing, discounts, product costs, or demand are contributing to their negative profitability.

### 4. Monthly Profitability

Profitability varies across different months and years. Some periods generated strong profits, while others recorded negative profitability. For example:

- **October 2016:** ~$15,629 profit
- **January 2015:** negative profit
- **July 2014:** negative profit

**Finding:** The variation in monthly profitability suggests that factors such as seasonality, sales volume, discounts, product mix, and regional performance may influence business performance.

---

## 💡 Recommendations

### 1. Investigate Furniture Profitability

Furniture generates considerable sales but relatively low profit. Management should investigate:

- Discount levels
- Product costs
- Pricing
- Low-margin products
- Product mix

before focusing solely on increasing Furniture sales.

### 2. Prioritize High-Profit Categories

Technology and Office Supplies are stronger contributors to overall profit. Management should consider giving high-performing products within these categories greater attention through:

- Inventory availability
- Marketing
- Sales planning
- Targeted promotions

### 3. Investigate the Central Region

Since Central generated the lowest regional profit, management should investigate:

- Product mix
- Sales volume
- Discount levels
- Loss-making products
- Customer demand

The objective should be to identify the factors responsible for the weaker profitability.

### 4. Review Loss-Making Products

Products consistently generating negative profit should be reviewed before additional resources are allocated to them. Possible actions include:

- Reviewing selling prices
- Reducing excessive discounts
- Reviewing product costs
- Negotiating supplier costs
- Discontinuing consistently unprofitable products where appropriate

### 5. Investigate Low-Performing Months

Management should compare weaker months with stronger months to determine whether differences are caused by:

- Seasonality
- Sales volume
- Discounts
- Product mix
- Regional performance

Understanding these patterns can improve future sales and inventory planning.

### 6. Measure Profitability Alongside Sales

One of the key findings from this analysis is that **high sales do not automatically mean high profit**. Management should evaluate:

**Sales + Profit + Quantity + Discount + Profit Margin**

together when making business decisions.

---

## 📊 Dashboard

The final Excel dashboard provides an interactive overview of the retail business's sales and profitability performance.

**Key areas analyzed:**

- Overall Sales
- Overall Profit
- Profit by Region
- Profit by Category
- Monthly Profit Trend
- Product Performance
- Loss-Making Products

Slicers allow users to filter the dashboard and explore different segments of the dataset.

---

## 🛠️ Tools Used

**Microsoft Excel**

- Power Query
- PivotTables
- PivotCharts
- Slicers
- Excel Formulas
- Data Cleaning
- Data Visualization

**Skills Demonstrated**

- Data Cleaning
- Data Transformation
- Exploratory Data Analysis
- Profitability Analysis
- Sales Analysis
- Regional Analysis
- Product Analysis
- Trend Analysis
- Data Visualization
- Business Intelligence
- Business Recommendations