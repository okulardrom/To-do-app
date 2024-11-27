from optparse import Values

import functions
import FreeSimpleGUI as sg
label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip= "Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box,edit_button]],
                   font=('Helvetica', 20))# tienes que tener una list hecha de otras listas

while  True:#this keeps the program runing until breaking, allowint to keep ading inputs
    event, values = window.read()#if you hava a tuple like this , by creating 2
    ## variables you can store different elements of the tupple in each variable
    #print(1, event)
    #print(2, values)
    #print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            newto_do = values['todo'] + "\n"

            todos.append(newto_do)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo # replace item with selected index by new action
            functions.write_todos(todos)
            window['todos'].update(values=todos) # we are ponting to the list box key 'todos'
        case "todos":
            window['todo'].update(value=values['todos'][0])# we are referring to inputText instance key updates the name on the window



        case sg.WIN_CLOSED:
            break



window.close()
