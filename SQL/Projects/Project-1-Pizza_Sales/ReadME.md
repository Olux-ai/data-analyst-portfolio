# Pizza Sales Analysis: SQL

T-SQL queries that calculate the sales KPIs and chart datasets behind a Pizza Sales dashboard, using a single `pizza_sales` table covering **January – December 2015**.

The results of this analysis are visualized in the companion Power BI project: [Pizza Sales Dashboard (Power BI)](https://github.com/Olux-ai/data-analyst-portfolio/tree/main/PowerBI/Projects).

---

## Table of Contents

- [Business Questions](#business-questions)
- [Dataset](#dataset)
- [Tools and Skills](#tools-and-skills)
- [Query Catalog](#query-catalog)
- [Sample Queries](#sample-queries)
- [KPI Results](#kpi-results)
- [Findings](#findings)
- [How to Run](#how-to-run)
- [Questions to Explore Next](#questions-to-explore-next)
- [Repository Contents](#repository-contents)
- [Author](#author)

---

## Business Questions

The queries were written to answer the questions a sales dashboard needs to show:

1. How much revenue was generated, and how many orders and pizzas were sold?
2. What is the average order value, and how many pizzas does a customer buy per order?
3. Which days of the week and months of the year are the busiest?
4. How is revenue split across pizza categories and pizza sizes?
5. Which pizzas are the best and worst sellers by revenue, quantity, and number of orders?

---

## Dataset

| Item | Detail |
|---|---|
| Table | `pizza_sales` |
| Period | 1 January 2015 – 31 December 2015 |
| Source | [pizza_sales.csv](https://github.com/Olux-ai/data-analyst-portfolio/blob/main/PowerBI/Projects/Pizza-Sales/Dataset/pizza_sales.csv) |

Columns used in the queries:

| Column | Description |
|---|---|
| `order_id` | Unique identifier for each order (an order can contain several pizzas) |
| `order_date` | Date the order was placed |
| `pizza_name` | Name of the pizza |
| `pizza_category` | Category: Classic, Supreme, Chicken, or Veggie |
| `pizza_size` | Size: Regular, Medium, Large, X-Large, or XX-Large |
| `quantity` | Number of pizzas on the order line |
| `total_price` | Revenue for the order line |

---

## Tools and Skills

- **Language:** T-SQL (SQL Server)
- **Aggregation:** `SUM`, `COUNT`, `COUNT(DISTINCT ...)`, `GROUP BY`, `ORDER BY`
- **Window functions:** `SUM() OVER()` to calculate each group's share of total sales
- **Data types and dates:** `CAST`, `DATENAME`, `DATEPART`, `MONTH`
- **Ranking:** `TOP 5` with ascending and descending sorts for best and worst sellers

---

## Query Catalog

### A. KPIs

| # | KPI | Technique |
|---|---|---|
| 1 | Total Revenue | `SUM(total_price)` |
| 2 | Average Order Value | Total revenue divided by `COUNT(DISTINCT order_id)` |
| 3 | Total Pizzas Sold | `SUM(quantity)` |
| 4 | Total Orders | `COUNT(DISTINCT order_id)` |
| 5 | Average Pizzas per Order | Pizzas sold divided by total orders, using `CAST` to `DECIMAL` to avoid integer division |

### B. Chart Datasets

| # | Dataset | Technique |
|---|---|---|
| 1 | Daily trend for total orders | `DATENAME(DW, order_date)` with `COUNT(DISTINCT order_id)` |
| 2 | Monthly trend for total orders | `DATENAME(MM, order_date)` with `COUNT(DISTINCT order_id)` |
| 3 | Percentage of sales by pizza category | `SUM() OVER()` window function for share of total |
| 4 | Percentage of sales by pizza size | `SUM() OVER()` window function for share of total |
| 5 | Sales by pizza category | `GROUP BY pizza_category` |
| 6 | Top 5 pizzas by revenue, quantity, and orders | `TOP 5` with `ORDER BY ... DESC` |
| 7 | Bottom 5 pizzas by revenue, quantity, and orders | `TOP 5` with `ORDER BY ... ASC` |
| 8 | Top 5 pizzas by quantity | `TOP 5`, `SUM(quantity)` |
| 9 | Bottom 5 pizzas by quantity | `TOP 5`, `SUM(quantity)` |
| 10 | Top 5 pizzas by orders | `TOP 5`, `COUNT(DISTINCT order_id)` |
| 11 | Bottom 5 pizzas by orders | `TOP 5`, `COUNT(DISTINCT order_id)` |

The percentage queries (B3 and B4) can be filtered with a `WHERE` clause on `order_date` to look at a single month or quarter. Remove the filter to see the full-year split.

---

## Sample Queries

**Average Order Value**

```sql
SELECT SUM(total_price) / COUNT(DISTINCT order_id) AS [Avg Order Value]
FROM pizza_sales;
```

**Average Pizzas per Order** (casting to `DECIMAL` so the result is not rounded down to a whole number)

```sql
SELECT CAST(
         CAST(SUM(quantity) AS DECIMAL(10,2)) /
         CAST(COUNT(DISTINCT order_id) AS DECIMAL(10,2))
       AS DECIMAL(10,2)) AS [Average Pizza Per Order]
FROM pizza_sales;
```

**Daily trend for total orders**

```sql
SELECT DATENAME(DW, order_date) AS [Order Day],
       COUNT(DISTINCT order_id) AS [Total Orders]
FROM pizza_sales
GROUP BY DATENAME(DW, order_date)
ORDER BY [Total Orders];
```

**Percentage of sales by pizza category** (window function; add a `WHERE` clause to filter by period)

```sql
SELECT pizza_category,
       CAST(SUM(total_price) AS DECIMAL(10,2)) AS [Total Sales],
       CAST(SUM(total_price) * 100.0 / SUM(SUM(total_price)) OVER () AS DECIMAL(10,2)) AS PCT
FROM pizza_sales
GROUP BY pizza_category;
```

**Top 5 pizzas by revenue**

```sql
SELECT TOP 5 pizza_name,
       CAST(SUM(total_price) AS DECIMAL(10,2)) AS [Total Revenue],
       SUM(quantity) AS [Total Quantity],
       COUNT(DISTINCT order_id) AS [Total Orders]
FROM pizza_sales
GROUP BY pizza_name
ORDER BY [Total Revenue] DESC;
```

The full set of queries is in [`Pizza Sales SQL Queries.docx`](Pizza%20Sales%20SQL%20Queries.docx).

---

## KPI Results

Values for the full year (2015), as shown in the Power BI dashboard built on the same data:

| KPI | Value |
|---|---|
| Total Revenue | 817.86K |
| Average Order Value | 38.31 |
| Total Pizzas Sold | 49,574 |
| Total Orders | 21,350 |
| Average Pizzas per Order | 2.32 |

---

## Findings

Findings reported in the dashboard built from these queries:

- **Busiest day:** Friday, with about 3.5K orders. Sunday is the quietest day at about 2.6K.
- **Peak month:** July, with 1,935 orders.
- **Top category:** Classic, with 26.91% of sales and 14,888 pizzas sold.
- **Top size:** Large, with 38.24% of sales.
- **Best seller by revenue:** The Thai Chicken Pizza.
- **Best seller by quantity and orders:** The Classic Deluxe Pizza.
- **Lowest performer:** The Brie Carre Pizza ranks last for revenue, quantity, and orders.

---

## How to Run

1. Load the pizza sales dataset into a SQL Server database as a table named `pizza_sales`.
2. Open the queries from `Pizza Sales SQL Queries.docx` in your SQL client.
3. Run each query against the `pizza_sales` table.

The queries use SQL Server syntax (`TOP`, `DATENAME`, `DATEPART`). To run them on MySQL or PostgreSQL, replace `TOP 5` with `LIMIT 5`, and replace `DATENAME` and `DATEPART` with the equivalent date functions (for example `DAYNAME()` and `MONTHNAME()` in MySQL).

---

## Questions to Explore Next

Ideas for extending the analysis with the same table:

- Which hours of the day are busiest, using `order_time`?
- How does average order value differ by pizza size or category?
- Do the best-selling pizzas change month by month?
- Which pizzas sell in high quantity but generate low revenue?
- How much do the top 5 pizzas contribute to total revenue?

---

## Repository Contents

```text
SQL/Projects/Project-1-Pizza_Sales/
├── Pizza Sales SQL Queries.docx
└── README.md
```

---

## Author

**Adebayo Olumide Philip**

Entry-Level Data Analyst | Excel · SQL · Power BI · Python

- LinkedIn: [olumide-adebayo](https://www.linkedin.com/in/olumide-adebayo-9511932a0/)
- GitHub: [data-analyst-portfolio](https://github.com/Olux-ai/data-analyst-portfolio)
