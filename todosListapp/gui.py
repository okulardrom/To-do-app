import functions
import FreeSimpleGUI as sg
label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip= "Enter todo", key="todo")
add_button = sg.Button("Add")
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))# tienes que tener una list hecha de otras listas

while  True:#this keeps the program runing until breaking, allowint to keep ading inputs
    event, values = window.read()#if you hava a tuple like this , by creating 2
    ## variables you can store different elements of the tupple in each variable
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            newto_do = values['todo'] + "\n"

            todos.append(newto_do)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
