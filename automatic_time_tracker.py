from win32gui import GetWindowText, GetForegroundWindow
import os
import selenium
import plotly
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
    #bob2 = GetWindowText(GetForegroundWindow())
    while True:
        #active_window_name.append(GetWindowText(GetForegroundWindow()))
        bob2 = GetWindowText(GetForegroundWindow())
        bob = GetWindowText(GetForegroundWindow())
        if bob == bob2 and first:
            start = datetime.datetime.now()
            #print(start)
            timelist.append(start)

            first = False

        if bob != bob2 and not first:
            stop = datetime.datetime.now()
            timelist.append(stop)
            ovarall_time = stop - start
            print(ovarall_time)
            active_window_name.append(GetWindowText(GetForegroundWindow()))
            print(GetWindowText(GetForegroundWindow()) +": " + str(ovarall_time))
            first = True
        

except KeyboardInterrupt:
    stop = datetime.datetime.now()
    timelist.append(stop)
    print(stop)
    print(timelist)