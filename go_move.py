import time
import webbrowser

max_alerts = 3
total_alerts = 0

print("Started at: "+ time.ctime())
while total_alerts < max_alerts:
    time.sleep(10)
    webbrowser.open('https://www.github.com/EdwardMcConnell')
    total_alerts = total_alerts + 1

