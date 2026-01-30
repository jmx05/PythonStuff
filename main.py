#python list starts and ends with brackets, list is need to store multiple values in one variable
#you can print lists directly

#type() tells you what type a variable is

#numbers before variables aren't allowed
#input() allows the user to type something and you can directly store it in a variable


user_prompt = "Enter a task: " #you can save strings in variables and have them printed later

todos = []  #creates an empty list called todos
#True is a boolean data type
while True: #under the while condition, everything indented will be repeated infinitely True is True

    todo = input(user_prompt)
    print(todo.capitalize())  #capitalizes the first letter of the input 
    todos.append(todo)  #adds the value of todo to the end of the todos list
    print(todos)  #prints the current list of todos
