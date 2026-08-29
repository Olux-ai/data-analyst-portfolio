# Python Random Password Generator

A secure console-based password generator built with Python as my third project at DecodeLabs.

## Project Overview

This project generates random passwords based on a user-defined length.

The application uses Python modules for character selection and string manipulation to generate passwords containing lowercase letters, uppercase letters, numbers, and special characters.

The project was developed to strengthen my understanding of Python modules, functions, loops, input validation, string manipulation, and random character generation.

## Features

- Accepts a user-defined password length
- Validates password length
- Handles invalid user input
- Generates random passwords
- Includes lowercase letters
- Includes uppercase letters
- Includes numbers
- Includes special characters
- Guarantees at least one character from each required category
- Randomly shuffles generated characters
- Displays the generated password

## Technologies Used

- Python
- `string`
- `secrets`
- `random`

## Python Concepts Practiced

- Importing modules
- Variables
- Strings
- Lists
- Loops
- Conditional statements
- Functions
- Function parameters
- Return values
- `try` and `except`
- `ValueError`
- Input validation
- `secrets.choice()`
- `random.shuffle()`
- `range()`
- String manipulation
- List manipulation

## How It Works

The application follows these steps:

1. Ask the user for the desired password length.
2. Validate the input.
3. Select at least one lowercase letter.
4. Select at least one uppercase letter.
5. Select at least one number.
6. Select at least one special character.
7. Generate the remaining characters randomly.
8. Shuffle all characters.
9. Combine the characters into a password.
10. Display the generated password.

## Example

```text
Enter your password length: 12

Generated password: G7@kP2!xQ9mA
The generated password will vary because the characters are selected randomly.

Input Validation

The application prevents invalid password lengths such as:

0
-5
abc

For invalid input, the program displays an appropriate error message and asks the user to try again.

Challenges and Lessons Learned
1. Understanding Module Integration

I learned how different Python modules can be imported and combined to solve a specific problem.

For example:

import string
import secrets

The string module provides predefined character sets, while secrets is used for security-oriented random character selection.

2. Understanding Random Character Selection

I learned how secrets.choice() can be used to select individual characters from a collection.

3. Guaranteeing Password Complexity

One of the major improvements I made was ensuring that the generated password contains at least one lowercase letter, one uppercase letter, one number, and one special character.

This taught me the difference between simply generating random data and applying rules to the generated data.

4. Input Validation and Error Handling

I practiced handling invalid user input using try, except, and ValueError.

This helped me understand how to make programs more reliable and prevent them from crashing when users provide unexpected input.

5. Functions and Code Organization

I separated different responsibilities into functions, making the program easier to understand, maintain, and test.

6. Formatting and Code Structure

I continued to understand the importance of proper formatting and indentation in Python.

Good formatting makes code easier to read, understand, debug, and maintain.

What I Learned

This project strengthened my understanding of how Python modules, functions, loops, conditions, and data structures can work together to solve a real-world problem.

I also learned that writing a working program is only the beginning. Good programming requires validation, structure, readability, testing, and consideration of how the application behaves with different inputs.

Most importantly, this project improved my ability to think about a problem logically and break it down into smaller, manageable components.

Project Status

Completed

This project was developed as part of my Python learning journey at DecodeLabs.

Future Improvements

Possible future improvements include:

Generate multiple passwords at once
Allow users to customize character requirements
Add password strength evaluation
Add an option to copy the generated password
Build a graphical user interface
Add secure password storage where appropriate
Author

Adebayo Olumide Philip

Aspiring Data Analyst | Python | SQL | Excel | Power BI