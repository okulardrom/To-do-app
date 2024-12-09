import FreeSimpleGUI as sg
from convert_function import convert

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")
label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inch")
convert_button = sg.Button("Convert")
output_label = sg.Text("",key="output", text_color="red")

window = sg.Window("Convertor", layout=[[label1, input1],[label2, input2], [convert_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    n_inches = float(values["inch"])
    n_feet = float(values["feet"])
    meters = convert(n_feet, n_inches)
    window["output"].update(value=f"{meters} m")





window.close()