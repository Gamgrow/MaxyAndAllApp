from pathlib import Path

import PySimpleGUI as sg
import pandas as pd

# Add some color to the window


def exel():
    sg.theme('DarkTeal9')

    current_dir = Path(
        __file__).parent if '__file__' in locals() else Path.cwd()
    EXCEL_FILE = current_dir / 'Data_Entry.xlsx'
    df = pd.read_excel(EXCEL_FILE)

    layout = [
        [sg.Text('Please fill out the following fields:')],
        [sg.Text('Gmail', size=(15, 1)), sg.InputText(key='Name')],
        [sg.Text('Password', size=(15, 1)), sg.InputText(key='City')],


        [sg.Submit(), sg.Button('Clear'), sg.Exit()]
    ]

    window = sg.Window('Simple data entry form', layout)

    def clear_input():
        EXCEL_FILE.__delattr__
        for key in values:
            window[key]('')
           
        return None

    event, values = window.read()
    # if event == sg.WIN_CLOSED or event == 'Exit':
    #     axit()
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
        clear_input()
    window.close()




