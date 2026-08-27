def expense_tracker():
  expenses = []
  
  while True:
    expense = get_expense()
    if expense is None:
      break
  
  # Loop specifically for getting a valid description without numbers
    description = get_description()

    expenses.append({
      "description": description, 
      "amount": expense})
    
  if not expenses:
    print("\nNo expenses recorded.")
    return
      
  
  print("Expenses List:", expenses)
  
  print("\n---Expense History---")
  
  for i, item in enumerate(expenses, 1):
    print(f"{i}.{item['description']}: ${item['amount']:.2f}")
    
  summary = calculate_summary(expenses)
  
  print("\n---Your Expense Summary---")
  total = summary["total"]
  average = summary["average"]
  highest = summary["highest"]
  lowest = summary["lowest"]  

  print(f"Number of Expenses: {len(expenses)}")
  print(f"Highest Expenses: {highest['description']} (${highest['amount']:.2f})")
  print(f"Lowest Expenses: {lowest['description']} (${lowest['amount']:.2f})")
  print(f"Average Expenses: ${average:.2f}")
  print(f"Total Expenses: ${total:.2f}")
  

  
def calculate_total(expenses):
  total = 0
  for expense in expenses:
    total += expense["amount"]
  return total

def get_expense():
  while True:
    try:
      user_input = input("Enter expense amount or Enter 'done' to finish: ")
      
      if user_input == "done":
        return None
       
      expense = float(user_input)
      
      if expense <= 0:
        print("Amount must be greater than zero. Please try again.\n")
        continue
      
      return expense
      
      
    except ValueError: 
      print("Invalid input. Please enter a valid number for the amount\n")

def get_description():
  while True:
    description = input("Enter expense description: ").strip()
    if any(char.isdigit() for char in description):
      print("Description cannot contain numbers. Try again.")
    elif not description:
      print("Description cannot be empty. Try again.")
    else:
      return description
    
    
def calculate_summary(expenses):
  total = 0
  for expense in expenses:
    total += expense["amount"]
  highest = max(expenses, key=lambda x: x["amount"])
  lowest = min(expenses, key=lambda x: x["amount"])
  average = total / len(expenses) if expenses else 0
  
  return {
    "total": total,
    "average": average,
    "highest": highest,
    "lowest": lowest
  }
 
expense_tracker()
