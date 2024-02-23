import PySimpleGUI as sg

sg.theme("DarkBlack")
sg.set_options(font="Georgia 20", button_element_size=(4,2))
button_size = (4, 1)

layout = [
    [
        sg.Text(
            font="Georgia 34", 
            expand_x=True, 
            justification="right", 
            pad=(10,20), 
            key="-TEXT-"
        )
    ],
    [
        sg.Button(7, size=button_size), 
        sg.Button(8, size=button_size), 
        sg.Button(9, size=button_size), 
        sg.Button('/', expand_x=True, size=button_size)
    ],
    [
        sg.Button(4, size=button_size), 
        sg.Button(5, size=button_size), 
        sg.Button(6, size=button_size),
        sg.Button('*', size=button_size)
    ],
    [
        sg.Button(1, size=button_size), 
        sg.Button(2, size=button_size), 
        sg.Button(3, size=button_size), 
        sg.Button('-', expand_x=True, size=button_size)
    ],
    [
        sg.Button("00", size=button_size), 
        sg.Button(0, size=button_size), 
        sg.Button('.', size=button_size), 
        sg.Button('+', size=button_size)
    ],
    [
        sg.Button('C', expand_x=True, size=button_size), 
        sg.Button('=', expand_x=True, size=button_size)
    ]
]

window = sg.Window("Calculator", layout)

current_number = []
full_operation = []

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in ['.','00','0','1','2','3','4','5','6','7','8','9']:
        current_number.append(''.join(event))
        number_string = ''.join(current_number)
        window["-TEXT-"].update(number_string)

    if event in ['+','-','*','/']:
        full_operation.append(''.join(current_number))
        current_number = []
        full_operation.append(event)
        window["-TEXT-"].update(event)

    if event == '=':
        full_operation.append(''.join(current_number))
        try:
            answer = eval(''.join(full_operation))
            window["-TEXT-"].update(answer)
            full_operation = []
            current_number = str(answer)
        except:
            window["-TEXT-"].update("Error")

    if event == 'C':
        full_operation = []
        current_number = []
        window["-TEXT-"].update('')
        

window.close()
