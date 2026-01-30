#python list starts and ends with brackets, list is need to store multiple values in one variable
#you can print lists directly

#type() tells you what type a variable is

#numbers before variables aren't allowed
#input() allows the user to type something and you can directly store it in a variable


user_prompt = "Enter a task: " #you can save strings in variables and have them printed later

while True: #under the while condition, everything indented will be repeated infinitely True is True
    
    todo = input(user_prompt) 
    print("You have added the task:", todo)
