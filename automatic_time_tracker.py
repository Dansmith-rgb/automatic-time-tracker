from win32gui import GetWindowText, GetForegroundWindow
import os
import selenium
from plotly import offline
import subprocess
import time
import datetime
win = []
active_window_name = []
next_window_name = active_window_name
first = True
first2 = True
stop = datetime.datetime.now()
start = datetime.datetime.now()
timelist = []
try:
    while True:
        bob2 = GetWindowText(GetForegroundWindow())
        bob = GetWindowText(GetForegroundWindow())
        if bob == bob2 and first:
            start = datetime.datetime.now()
            first = False

        if bob != bob2 and not first:
            stop = datetime.datetime.now()
            ovarall_time = stop - start
            timelist.append(str(ovarall_time))
            print(ovarall_time)
            active_window_name.append(GetWindowText(GetForegroundWindow()))
            text = print(GetWindowText(GetForegroundWindow()))
            if text == "":
                print("Couldn't get data")

            first = True
        

except KeyboardInterrupt:
    stop = datetime.datetime.now()
    ovarall_time = stop - start
    timelist.append(str(ovarall_time))
    print(stop)
    print(timelist)

    def graph_data(active_window_name, timelist):
        data = [{
            'type': 'bar',
            'x': active_window_name,
            'y': timelist,
            'marker': {
                'color': 'rgb(0, 100, 0)',
            }
        }]

        my_layout = {
            'title': 'time on applications',
            'xaxis': {'title': 'applications'},
            'yaxis': {'title': 'time'}
        }

        fig = {'data': data, 'layout': my_layout}
        offline.plot(fig, filename='application_data.html')
    graph_data(active_window_name, timelist)


