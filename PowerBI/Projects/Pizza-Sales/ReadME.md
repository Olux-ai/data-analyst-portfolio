# Pizza Sales Dashboard: Power BI

An interactive two-page Power BI report that analyzes **2015 pizza sales**. It tracks revenue, orders, and customer buying behavior, shows when sales peak, and ranks the best and worst performing pizzas.

The SQL queries used to define the KPIs and chart datasets are in the companion project: [Pizza Sales Analysis: SQL](https://github.com/Olux-ai/data-analyst-portfolio/tree/main/SQL/Projects/Project-1-Pizza_Sales).

---

## Table of Contents

- [Dashboard Preview](#dashboard-preview)
- [Business Questions](#business-questions)
- [Dataset](#dataset)
- [Report Structure](#report-structure)
- [Data Model and DAX](#data-model-and-dax)
- [Key Findings](#key-findings)
- [Tools and Skills](#tools-and-skills)
- [How to Open the Project](#how-to-open-the-project)
- [Questions to Explore Next](#questions-to-explore-next)
- [Repository Contents](#repository-contents)
- [Author](#author)

---

## Dashboard Preview

### Page 1: Home

![Home dashboard](https://raw.githubusercontent.com/Olux-ai/data-analyst-portfolio/main/PowerBI/Projects/Pizza-Sales/ScreenShot/Home%20Dashboard.png)

### Page 2: Best / Worst Sellers

![Best and worst sellers dashboard](https://raw.githubusercontent.com/Olux-ai/data-analyst-portfolio/main/PowerBI/Projects/Pizza-Sales/ScreenShot/Best-Worst%20Sellers%20Dashboard.png)

---

## Business Questions

1. How much revenue did the business generate, and how many orders and pizzas were sold?
2. What is the average order value, and how many pizzas does a typical order contain?
3. Which days of the week and months of the year are the busiest?
4. Which pizza categories and sizes contribute the most to sales?
5. What percentage of total sales does each pizza size contribute?
6. Which pizzas are the best and worst sellers by revenue, quantity, and orders?

---

## Dataset

| Item | Detail |
|---|---|
| Table | `pizza_sales` |
| Period | 1 January 2015 – 31 December 2015 |
| Source | [pizza_sales.csv](https://github.com/Olux-ai/data-analyst-portfolio/blob/main/PowerBI/Datasets/pizza_sales.csv) |

Main fields: `order_id`, `order_date`, `order_time`, `pizza_id`, `pizza_name_id`, `pizza_name`, `pizza_category`, `pizza_size`, `pizza_ingredients`, `quantity`, `total_price`.

---

## Report Structure

### Page 1: Home

| Section | Content |
|---|---|
| Filters | Date range slicer (2015) and Pizza Category slicer (Chicken, Classic, Supreme, Veggie) |
| KPI cards | Total Revenue, Avg Order Value, Total Pizza Sold, Total Orders, Avg Pizza Per Order |
| Daily trend | Column chart of total orders by day of the week |
| Monthly trend | Line/area chart of total orders by month |
| Sales by category | Donut chart showing percentage of sales by pizza category |
| Sales by size | Donut chart showing percentage of sales by pizza size |
| Pizzas sold by category | Funnel chart of total pizzas sold per category |
| Insight panel | Text summaries of the busiest days and times and the top category and size |

### Page 2: Best / Worst Sellers

| Section | Content |
|---|---|
| Filters and KPIs | Same date range and category slicers and KPI cards as the Home page |
| Best sellers | Top 5 pizzas by revenue, by quantity, and by orders (bar charts) |
| Worst sellers | Bottom 5 pizzas by revenue, by quantity, and by orders (bar charts) |
| Insight panel | Text summaries naming the top and bottom pizza in each measure |

### Interactivity

- Date range and category slicers filter every visual on the page.
- Navigation buttons (Home / Best/Worst Sellers) move between pages.
- KPI cards and charts respond to slicer selections, so the whole report can be filtered by category or period.

---

## Data Model and DAX

The report uses a single `pizza_sales` table with calculated columns and measures added for reporting.

**Date fields used for labels and sorting**

| Field | Purpose |
|---|---|
| `Day Name` | Day of the week for each order |
| `Days Number` | Numeric day used to sort days in weekday order |
| `Month Name` | Month name for each order |
| `Month Number` | Numeric month used to sort months in calendar order |

**Calculated columns**

| Column | Purpose |
|---|---|
| `Order Days` | Three-letter day label for chart axes (SUN, MON, ...) |
| `Order Month` | Three-letter month label for chart axes (JAN, FEB, ...) |

```DAX
Order Days = UPPER(LEFT(pizza_sales[Day Name], 3))
```

The text labels are sorted with **Sort by column** using `Days Number` and `Month Number`, so the axes show days in weekday order and months in calendar order instead of alphabetical order.

**Measures**

| Measure | Definition |
|---|---|
| Total Revenue | Sum of `total_price` |
| Avg Order Value | Total revenue divided by the number of distinct orders |
| Total Pizza Sold | Sum of `quantity` |
| Total Orders | Distinct count of `order_id` |
| Avg Pizza Per Order | Total pizzas sold divided by total orders |

---

## Key Findings

- **Total performance (2015):** 817.86K in revenue from 21,350 orders and 49,574 pizzas sold, with an average order value of 38.31 and 2.32 pizzas per order.
- **Busiest day:** Friday, with about 3.5K orders. Sunday is the quietest day at about 2.6K.
- **Peak month:** July, with 1,935 orders. October is the lowest at 1,646.
- **Category:** Classic contributes the most to sales at 26.91%, followed by Supreme (25.46%), Chicken (23.96%), and Veggie (23.68%).
- **Size:** Large pizzas account for 38.24% of sales, followed by Medium (31.54%) and Regular (29.05%). X-Large and XX-Large together contribute about 1%.
- **Best sellers:** The Thai Chicken Pizza generates the most revenue, and The Classic Deluxe Pizza leads on quantity and orders.
- **Worst seller:** The Brie Carre Pizza ranks last on revenue, quantity, and orders.

---

## Tools and Skills

- **Power BI Desktop** (`.pbix` and Power BI Project `.pbip` formats)
- **Data modeling and transformation:** calculated columns, sort-by-column, data type formatting
- **DAX:** measures and calculated columns
- **Visualization and design:** KPI cards, column, line/area, donut, funnel, and bar charts, slicers, page navigation, custom layout and theme
- **SQL (T-SQL):** KPI and chart datasets defined in the companion SQL project

---

## How to Open the Project

1. Clone or download this repository.
2. Open `pizza-sales.pbix` in **Power BI Desktop**. The Power BI Project version (`pizza-sales.pbip`) is also included.
3. If prompted, update the data source connection to point to your local copy of the [`pizza_sales.csv`](https://github.com/Olux-ai/data-analyst-portfolio/blob/main/PowerBI/Datasets/pizza_sales.csv) dataset, then select **Refresh**.

The `.pbip` version requires a recent version of Power BI Desktop with Power BI Project (PBIP) support enabled.

---

## Questions to Explore Next

Ideas for extending the report:

- Add an hour-of-day view using `order_time` to identify peak service hours.
- Compare average order value across categories and sizes.
- Add a month-over-month growth measure.
- Add an ingredients analysis using `pizza_ingredients` to see which toppings appear in the best sellers.
- Add tooltips or drill-through pages for individual pizzas.

---

## Repository Contents

```text
PowerBI/
├── Datasets/
│   └── pizza_sales.csv
└── Projects/
    └── Pizza-Sales/
        ├── ScreenShot/
        │   ├── Home Dashboard.png
        │   └── Best-Worst Sellers Dashboard.png
        ├── pizza-sales.pbix
        ├── pizza-sales.pbip
        ├── pizza-sales.Report/
        ├── pizza-sales.SemanticModel/
        └── README.md
```

---

## Author

**Adebayo Olumide Philip**

Entry-Level Data Analyst | Excel · SQL · Power BI · Python

- LinkedIn: [olumide-adebayo](https://www.linkedin.com/in/olumide-adebayo-9511932a0/)
- GitHub: [data-analyst-portfolio](https://github.com/Olux-ai/data-analyst-portfolio)
