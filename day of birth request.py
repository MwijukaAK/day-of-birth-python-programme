import calendar
import time
from datetime import date
today=date.today()
age=input("How old are you now: \n")
int_age=int(age)
birthyear=today.year-int_age
endings=["st","nd","rd"] + 17*["th"]+["st","nd","rd"] + 7*["th"] + ["st"]
month=input("In what month were you born (1-12): \n")
day=input("On what day were you born (1-31): \n")
month_number =int(month)
day_number = int(day)
actual_month=calendar.month_name[month_number]
ordinal = day + endings[day_number -1]
my_birthday=date(today.year, month_number, day_number)
if my_birthday < today:
    birthdaydate=calendar.day_name[calendar.weekday(birthyear,month_number,day_number)]
    print("you were born on ",birthdaydate,ordinal,actual_month,birthyear)
else:
    birthyear=birthyear -1
    birthdaydate=calendar.day_name[calendar.weekday(birthyear,month_number,day_number)]
    print("you were born on ",birthdaydate,ordinal,actual_month,birthyear)

    
    
    
