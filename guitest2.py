import PySimpleGUI as sg

# ----------- Create the 3 layouts this Window will display -----------
layout_start = [[sg.Text('This is layout 3 - It is all Radio Buttons')],
           *[[sg.Button(f'Radio {i}')] for i in range(8)]]

layout2 = [[sg.Text('This is layout 2')],
           [sg.Input(key='-IN-')],
           [sg.Input(key='-IN2-')]]

layout3 = [[sg.Text('This is layout 3 - It is all Radio Buttons')],
           *[[sg.Button(f'Radio {i}', 1)] for i in range(8)]]

# ----------- Create actual layout using Columns and a row of Buttons
current_layout = layout_start

window = sg.Window('Swapping the contents of a window', layout_start)

layout = 1  # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Cycle Layout':
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout + 1 if layout < 3 else 1
        window[f'-COL{layout}-'].update(visible=True)

    elif event == 'Radio 1':
        window.close()
        window = sg.Window('Swapping the contents of a window', layout2)

    elif event in '123':
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)
window.close()