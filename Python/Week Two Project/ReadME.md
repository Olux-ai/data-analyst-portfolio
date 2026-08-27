\# Python Expense Tracker



A console-based Expense Tracker built with Python as my second project at DecodeLabs.



\## Project Overview



The Expense Tracker allows users to record expenses, provide descriptions, and view a summary of their spending.



The project was developed to strengthen my understanding of Python fundamentals, data structures, input validation, exception handling, functions, and basic data processing.



\## Features



\- Add and record expenses

\- Add descriptions to expenses

\- Validate expense amounts

\- Validate expense descriptions

\- Handle invalid user input

\- View expense history

\- Calculate total spending

\- Calculate average expense

\- Identify the highest expense

\- Identify the lowest expense

\- Display the number of recorded expenses



\## Technologies Used



\- Python

\- Python Standard Library





\## Python Concepts Practiced



\- Variables and data types

\- Lists

\- Dictionaries

\- Loops

\- Conditional statements

\- Functions

\- Function parameters

\- Return values

\- Exception handling

\- Input validation

\- `append()`

\- `enumerate()`

\- `len()`

\- `max()` and `min()`

\- Lambda functions

\- Accumulator pattern

\- Basic descriptive statistics



\## Data Structure



Each expense is stored as a dictionary inside a list:



```python

expenses = \[

&#x20;   {

&#x20;       "description": "Food",

&#x20;       "amount": 100

&#x20;   },

&#x20;   {

&#x20;       "description": "Transport",

&#x20;       "amount": 50

&#x20;   }

]



\--- Expense History ---



1\. Food: $100.00

2\. Transport: $50.00

3\. Data: $25.00



Number of Expenses: 3

Highest Expense: Food ($100.00)

Lowest Expense: Data ($25.00)

Average Expense: $58.33

Total Spent: $175.00



Challenges and Lessons Learned



During the development of this project, I encountered several challenges that helped improve my Python programming skills.



1\. Understanding Accumulators



I learned how to continuously add values to a variable using an accumulator:



total += expense\["amount"]



This helped me understand how data can be processed progressively.



2\. Working with Lists of Dictionaries



I learned how to store structured records by combining lists and dictionaries. This allowed me to keep both the description and amount of each expense.



3\. Input Validation and Exception Handling



I learned how to validate user input and use try and except to prevent invalid input from crashing the application.



4\. Functions and Code Organization



I learned the importance of breaking a program into smaller functions, with each function having a specific responsibility. This made the code easier to understand, test, and maintain.



5\. Formatting and Indentation



One of my important lessons from this project was understanding how important formatting and indentation are in programming.



Python relies heavily on indentation to define blocks of code. I learned that proper formatting is not only about making code look clean; it can directly affect how the program works and can help prevent logical and syntax errors.



What I Learned



This project strengthened my ability to use Python to collect, structure, process, and analyze data.



I also gained a better understanding of how individual programming concepts work together to build a complete application.



Most importantly, the project helped me move from simply writing individual lines of Python code to thinking about program structure, data processing, validation, and problem-solving.



Project Status



Completed



This project was developed as part of my Python learning journey at DecodeLabs.



Future Improvements



Possible future improvements include:



Expense categories

Date tracking

Monthly expense analysis

Category-based analysis

CSV export

Database integration

Graphical user interface



Author



Adebayo Olumide Philip



Aspiring Data Analyst | Python | SQL | Excel | Power BI

