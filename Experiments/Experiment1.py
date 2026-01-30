user_prompt = "Enter a task: " #you can save strings in variables and have them printed later

toods = []

while True: #under the while condition, everything indented will be repeated infinitely True is True

    todo = input(user_prompt)
    print(todo.title())  #capitalizes the first letter of the input 
    toods.append(todo)  #adds the value of todo to the end of the toods list
  