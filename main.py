user_prompt = "Enter a task: " #you can save strings in variables and have them printed later

todo1 = input(user_prompt) #input() allows the user to type something and you can directly store it in a variable
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3] #python list starts and ends with brackets, list is need to store multiple values in one variable
print(todos) #you can print lists directly

print(type(todos)) #type() tells you what type a variable is

#numbers before variables aren't allowed