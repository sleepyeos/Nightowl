#! /usr/bin/env python

# NIGHTOWL FREELANCER TIMECLOCK V0.1

import PySimpleGUI as sg
import csv
from datetime import datetime

timecard = None
header = ['time', 'type']

class NightOwl:
    def __init__(self):
        self.init_gui()

    def init_gui(self):
        sg.theme('DarkBlue2')
        self.layout = [

            [sg.Text('TOTAL: '), sg.Text('00:00:00', key='timedisplay')],
            [sg.Output(size = (50, 20))],
            [sg.Button('In'), sg.Button('Out')],
            [sg.Button('Load'), sg.Button('New'), sg.Button('Exit')]
        ]

        window = sg.Window('NIGHTOWL v1.0', self.layout)

        while True:
            event, value = window.read()
            if event is None or event == 'Exit':
                break;
            if event == 'Load':
                timecard = sg.popup_get_file('Open Timecard', no_window=True)
            if event == 'New':
                pass
            if event in ['In', 'Out']:
                if timecard is None:
                    sg.PopupError('Please create or load a timecard.')
            if event == 'In':
                if timecard is not None:
                    rows = [{'time':str(datetime.now()),
                                               'type': 'IN'}]
                    with open(timecard, 'a') as f:
                        csv_writer = csv.DictWriter(f, fieldnames=header)
                        csv_writer.writerows(rows)
                    print(rows)
            if event == 'Out':
                if timecard is not None:
                    rows = [{'time':str(datetime.now()),
                                               'type': 'OUT'}]
                    with open(timecard, 'a') as f:
                        csv_writer = csv.DictWriter(f, fieldnames=header)
                        csv_writer.writerows(rows)
                    print(rows)
            
        
no = NightOwl()
