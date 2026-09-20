\# Pizza Sales Dashboard: Power BI



An interactive two-page Power BI report that analyzes \*\*2015 pizza sales\*\*. It tracks revenue, orders, and customer buying behavior, shows when sales peak, and ranks the best and worst performing pizzas.



The SQL queries used to define the KPIs and chart datasets are in the companion project: \[Pizza Sales Analysis: SQL](https://github.com/Olux-ai/data-analyst-portfolio/tree/main/SQL/Projects/Project-1-Pizza\_Sales).



\---



\## Table of Contents



\- \[Dashboard Preview](#dashboard-preview)

\- \[Business Questions](#business-questions)

\- \[Dataset](#dataset)

\- \[Report Structure](#report-structure)

\- \[Data Model and DAX](#data-model-and-dax)

\- \[Key Findings](#key-findings)

\- \[Tools and Skills](#tools-and-skills)

\- \[How to Open the Project](#how-to-open-the-project)

\- \[Questions to Explore Next](#questions-to-explore-next)

\- \[Repository Contents](#repository-contents)

\- \[Author](#author)



\---



\## Dashboard Preview



\### Page 1: Home



!\[Home dashboard](https://github.com/Olux-ai/data-analyst-portfolio/blob/main/PowerBI/Projects/Pizza-Sales/ScreenShot/Home%20Dashboard.png)



\### Page 2: Best / Worst Sellers



!\[Best and worst sellers dashboard](https://github.com/Olux-ai/data-analyst-portfolio/blob/main/PowerBI/Projects/Pizza-Sales/ScreenShot/Best-Worst%20Sellers%20Dashboard.png)



\---



\## Business Questions



1\. How much revenue did the business generate, and how many orders and pizzas were sold?

2\. What is the average order value, and how many pizzas does a typical order contain?

3\. Which days of the week and months of the year are the busiest?

4\. Which pizza categories and sizes contribute the most to sales?

5\. The total percentage of Sales by pizza size?

6\. Which pizzas are the best and worst sellers by revenue, quantity, and orders?



\---



\## Dataset



| Item | Detail |

|---|---|

| Table | `pizza\_sales` |

| Period | 1 January 2015 – 31 December 2015 |

| Source | \*(add dataset name /https://github.com/Olux-ai/data-analyst-portfolio/blob/main/PowerBI/Datasets/pizza\_sales.csv)\* |



Main fields: `order\_id`, `order\_date`, `order\_time`, `pizza\_id`, `pizza\_name\_id`, `pizza\_name`, `pizza\_category`, `pizza\_size`, `pizza\_ingredients`, `quantity`, `total\_price`.



\---



\## Report Structure



\### Page 1: Home



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



\### Page 2: Best / Worst Sellers



| Section | Content |

|---|---|

| Filters and KPIs | Same date range and category slicers and KPI cards as the Home page |

| Best sellers | Top 5 pizzas by revenue, by quantity, and by orders (bar charts) |

| Worst sellers | Bottom 5 pizzas by revenue, by quantity, and by orders (bar charts) |

| Insight panel | Text summaries naming the top and bottom pizza in each measure |



\### Interactivity



\- Date range and category slicers filter every visual on the page.

\- Navigation buttons (Home / Best/Worst Sellers) move between pages.

\- KPI cards and charts respond to slicer selections, so the whole report can be filtered by category or period.



\---



\## Data Model and DAX



The report uses a single `pizza\_sales` table with calculated columns and measures added for reporting.



\*\*Date fields used for labels and sorting\*\*



| Field | Purpose |

|---|---|

| `Day Name` | Day of the week for each order |

| `Days Number` | Numeric day used to sort days in weekday order |

| `Month Name` | Month name for each order |

| `Month Number` | Numeric month used to sort months in calendar order |



\*\*Calculated columns\*\*



| Column | Purpose |

|---|---|

| `Order Days` | Three-letter day label for chart axes (SUN, MON, ...) |

| `Order Month` | Three-letter month label for chart axes (JAN, FEB, ...) |



```DAX

Order Days = UPPER(LEFT(pizza\_sales\[Day Name], 3))

```



The text labels are sorted with \*\*Sort by column\*\* using `Days Number` and `Month Number`, so the axes show days in weekday order and months in calendar order instead of alphabetical order.



\*\*Measures\*\*



| Measure | Definition |

|---|---|

| Total Revenue | Sum of `total\_price` |

| Avg Order Value | Total revenue divided by the number of distinct orders |

| Total Pizza Sold | Sum of `quantity` |

| Total Orders | Distinct count of `order\_id` |

| Avg Pizza Per Order | Total pizzas sold divided by total orders |



\---



\## Key Findings



\- \*\*Total performance (2015):\*\* 817.86K in revenue from 21,350 orders and 49,574 pizzas sold, with an average order value of 38.31 and 2.32 pizzas per order.

\- \*\*Busiest day:\*\* Friday, with about 3.5K orders. Sunday is the quietest day at about 2.6K.

\- \*\*Peak month:\*\* July, with 1,935 orders. October is the lowest at 1,646.

\- \*\*Category:\*\* Classic contributes the most to sales at 26.91%, followed by Supreme (25.46%), Chicken (23.96%), and Veggie (23.68%).

\- \*\*Size:\*\* Large pizzas account for 38.24% of sales, followed by Medium (31.54%) and Regular (29.05%). X-Large and XX-Large together contribute about 1%.

\- \*\*Best sellers:\*\* The Thai Chicken Pizza generates the most revenue, and The Classic Deluxe Pizza leads on quantity and orders.

\- \*\*Worst seller:\*\* The Brie Carre Pizza ranks last on revenue, quantity, and orders.



\---



\## Tools and Skills



\- \*\*Power BI Desktop\*\* (Power BI Project format, `.pbip`)

\- \*\*Data modeling and transformation:\*\* calculated columns, sort-by-column, data type formatting

\- \*\*DAX:\*\* measures and calculated columns

\- \*\*Visualization and design:\*\* KPI cards, column, line/area, donut, funnel, and bar charts, slicers, page navigation, custom layout and theme

\- \*\*SQL (T-SQL):\*\* KPI and chart datasets defined in the companion SQL project



\---



\## How to Open the Project



1\. Clone or download this repository.

2\. Open `pizza-sales.pbip` in \*\*Power BI Desktop\*\*.

3\. If prompted, update the data source connection to point to your local copy of the `pizza\_sales` dataset, then select \*\*Refresh\*\*.



Power BI Project files (`.pbip`) require a recent version of Power BI Desktop with Power BI Project (PBIP) support enabled.
The (`.pbix`) files is now included.



\---



\## Repository Contents



```

PowerBI/Projects/

├── pizza-sales.pbip

├── pizza-sales.Report/

├── pizza-sales.SemanticModel/

├── images/

│   ├── Home\_Dashboard.png

│   └── Best-Worst\_Sellers\_Dashboard.png

└── README.md

```



\---



\## Author



\*\*Adebayo Olumide Philip\*\*

Entry-Level Data Analyst | Excel · SQL · Power BI · Python



\[LinkedIn](https://www.linkedin.com/in/olumide-adebayo-9511932a0/) · \[GitHub Portfolio](https://github.com/Olux-ai/data-analyst-portfolio)

