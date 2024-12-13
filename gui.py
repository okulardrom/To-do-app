import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todosListapp/todos.txt"):
    with open("todosListapp/todos.txt", "w") as file:
        pass


sg.theme("DarkBlack")

clock = sg.Text('', key='timer')
label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip= "Enter todo", key="todo")
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="#8CAE7F",
                       tooltip="Add to do", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(size=2, image_source="complete.png", mouseover_colors="#E4080A",
                            tooltip="Complete todo", key="Complete")
exit_button = sg.Button("Exit")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
window = sg.Window('My To-Do App',
                   layout= layout,
                   font=('Helvetica', 20))# tienes que tener una list hecha de otras listas

while  True:#this keeps the program runing until breaking, allowint to keep ading inputs
    event, values = window.read(timeout=200)#if you hava a tuple like this , by creating 2
    ## variables you can store different elements of the tupple in each variable
    #print(1, event)
    #print(2, values)
    #print(3, values['todos'])
    now = time.strftime("%b %d, %Y %H: %M: %S")
    window["timer"].update(value=now)
    match event:
        case "Add":
            todos = functions.get_todos()
            newto_do = values['todo'] + "\n"

            todos.append(newto_do)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo # replace item with selected index by new action
                functions.write_todos(todos)
                window['todos'].update(values=todos) # we are ponting to the list box key 'todos'
            except IndexError:
                sg.popup("please select an item first", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("please select an item first", font=("Helvetica", 20))
        case "Exit":
            break


        case "todos":
            window['todo'].update(value=values['todos'][0])# we are referring to inputText instance key updates the name on the window



        case sg.WIN_CLOSED:
            break


print("Bye")
window.close()
