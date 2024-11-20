import random
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


def getTodos(filepath='files/todos.txt'):
    """ Read a text file and return a list of 
    todo items.
    """ #this is a doc string , helps to show the usage of the function in the help() function
    with open(filepath,'r') as file_local:  # with this with context does waht the comment lines above but you dont have to close it, ensures that the file wont remain open
        todos_local = file_local.readlines()

    return todos_local
#print(help(getTodos))

def writeTodos(todos_arg, filepath='files/todos.txt'): #none defaul parameters cant follow defualt parameters , that is the reason the parms assigned default are after the parm with no assignation
    """ Writes to do items list in to-do file """
    with open(filepath, 'w') as file_local:
         file_local.writelines(todos_arg)
#this function overides but returns nothing to the user so we dont use return we use it as a procedure




while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith('add'): # the in operator heps to check uif a condition is true or exists whit in  a string
        todo = user_action[4:]#list slicing  everything that comes after the 'add' [4:9] we are picking the charters that occupy the position from 4 to 8

        todos = getTodos() # using the new function we created

        todos.append(todo + '\n') #appends strings bug fixed adding a break line

        #file = open('files/todos.txt', 'w')
        #file.writelines(todos)
        #file.close()
        writeTodos(todos) #we dont have to add file path since filepath is already defined




    elif user_action.startswith('show'):

        todos = getTodos()  # using the new function we created

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

            todos = getTodos()  # using the new function we created


            new_todo = input("enter new todo: ")
            todos[number]= new_todo + '\n' #gets the chosen index of the variable and overrides it with new string
            writeTodos(todos, 'files/todos.txt')
        except ValueError:
            print("Your command is not valid")
            continue # the opposite of break it  takes you back to the begining

    elif user_action.startswith('complete'):
        try:
            item_remove = int(user_action[9:])

            todos = getTodos()  # using the new function we created

            index_complete = item_remove - 1
            todo_to_remove = todos[index_complete].strip('\n')

            todos.pop(index_complete)

            writeTodos(todos)
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



