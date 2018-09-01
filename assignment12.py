#question number one
from datetime import date
import calendar
my_date=date.today()
print(calendar.day_name[my_date.weekday()])

#question number two
import webbrowser
import time
total_breaks=1
break_count=0
while(break_count<total_breaks):
    print("this program started on "+time.ctime())
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=3Bx1aW2fqnY")
    break_count+=1

#question number three
import os
path ='C:/Users/Pawanpreet Kaur/Desktop/directory'
files =os.listdir(path)
i=1
for file in files:
    os.rename(os.path.join(path,file),os.path.join(path,str(i)+'.jpg'))
    i=i+1
