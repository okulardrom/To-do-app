#file = open(r"D:\tiorogelio") you ned to create a row string  with the r  in the begining  cuz backslash +t
#is a function, that way you transform everything as a string that only happens in windows. for absolut paths
user_prompt = """chose an option 
1.- add/new
2.- show
3.- edit
4.- complete
5.- exit


"""


print(user_prompt.capitalize())


while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith('add'): # the in operator heps to check uif a condition is true or exists whit in  a string
        todo = user_action[4:]#list slicing  everything that comes after the 'add' [4:9] we are picking the charters that occupy the position from 4 to 8

        #file = open('files/todos.txt', 'r')
        #todos = file.readlines()
        #file.close()

        with open('files/todos.txt', 'r') as file: # with this with context does waht the comment lines above but you dont have to close it, ensures that the file wont remain open
            todos = file.readlines()


        print(todo.capitalize())

        todos.append(todo + '\n') #appends strings bug fixed adding a break line

        #file = open('files/todos.txt', 'w')
        #file.writelines(todos)
        #file.close()
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)



    elif user_action.startswith('show'):
        file = open('files/todos.txt', 'r')
        todos = file.readlines() # this method returns a list
        file.close()
        #new_todos = []
        #for item in todos:
           # new_item = item.strip('\n')#removes a part of and element of the list , in this case the for loop makes it for each element
           # new_todos.append(new_item)
        #new_todos = [item.strip('\n') for item in todos] # a 'list comprehension' iterates with a forloop on a newly declared list variable and apply a function operation in 1 line

        for index, item in enumerate(todos):
            item = item.strip('\n') # this is an even faster way to change the extra space as  in the commented lines but easier
            index = index + 1
            item = item.title()
            tasks = f"{index} .- {item}" # f string example it adds variables inside strings
            print(tasks)
        print('number of items',len(todos))
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()


            new_todo = input("enter new todo: ")
            todos[number]= new_todo + '\n' #gets the chosen index of the variable and overrides it with new string
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue # the opposite of break it  takes you back to the begining

    elif user_action.startswith('complete'):
        try:
            item_remove = int(user_action[9:])

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            index_complete = item_remove - 1
            todo_to_remove = todos[index_complete].strip('\n')

            todos.pop(index_complete)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("that item  doesnt exist")
            continue
        except ValueError:
            print("please enter a correct value:")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("command is not valid")


print("bye!")



