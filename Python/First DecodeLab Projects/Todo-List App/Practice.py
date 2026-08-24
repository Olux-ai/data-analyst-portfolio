import json

""" with open("test.txt", "a") as file:
  file.write("I am learning Python.")
  file.write("By Olumide Adebayo")
  
  with open("test.txt", "r") as file:
    content = file.read()
    print(content) """
    

todo_list = [
  {
  "task": "Learn Python", 
  "Status": "Pending"},
  {
    "task": "Practice SQL",
    "Status": "Completed"}
]

with open("todo.json", "w")  as file:
  json.dump(todo_list, file, indent=2)
  
  
""" with open("todo.json", "r") as file:
  todo_list = json.load(file)
    
print(todo_list) """