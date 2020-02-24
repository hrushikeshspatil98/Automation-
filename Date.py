import datetime;  
from datetime import datetime as dt
#Get current date and time
strDateTime= datetime.datetime.now()
print("Date and Time:",strDateTime)  

#To get day,month,year from date
print("Date: "+str(strDateTime.day)+"-"+str(strDateTime.month)+"-"+str(strDateTime.year))
#To get hour,minutes,seconds from time
print("Time: "+str(strDateTime.hour)+":"+str(strDateTime.minute)+":"+str(strDateTime.second))

weekDay=strDateTime.weekday()
wdswitcher = {
        0: "Monday", 1: "Tuesday",2: "Wednesday",
        3: "Thursday",4: "Friday",5: "Saturday",6: "Sunday"
    }
print("Day of week is: ",wdswitcher.get(weekDay))

moyswitcher = {
        1: "January",2: "February",3: "March",4: "April",
        5: "May",6: "June",7: "July",8: "August",
        9: "September",10: "October",11: "November",12: "December"
    }
print("Month of the year:",moyswitcher.get(strDateTime.month))

#Creating custom date objects
print("Enter current day, month, year one by one:")
day=int(input())
month=int(input())
year=int(input())
userInpDate=datetime.datetime(year,month,day)
print("User Date: ",userInpDate)
#Getting Week of the Year
print(userInpDate.isocalendar())
#Compare two dates
if dt(dt.now().year,dt.now().month,dt.now().day,9)<userInpDate.now()<dt(dt.now().year,dt.now().month,dt.now().day,18):  
    print("Working hours")  
else:  
    print("Non Working hours")  

"""Output:
Date and Time: 2020-02-24 12:18:37.129015
Date: 24-2-2020
Time: 12:18:37
Day of week is:  Monday
Month of the year: February
Enter current day, month, year one by one:
24
2
2020
User Date:  2020-02-24 00:00:00
(2020, 9, 1)
Working hours
"""
