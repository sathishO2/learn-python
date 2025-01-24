# Datetime Package

'''
Write a function that takes two dates as strings in the format 'YYYY-MM-DD' and returns the number of days between them.
'''
from datetime import datetime

def deff_of_days(s1,s2):
    deff = datetime.fromisoformat(s2) - datetime.fromisoformat(s1)
    # print("days:",deff.days)
    return deff.days

s1 = '2023-05-31'
s2 = '2024-06-06'
r = deff_of_days(s1,s2)
print(r)

'''
Create a function that takes a datetime object and returns a string representing the date and time in the format 'DD/MM/YYYY HH:MM
'''
import datetime
def q2(dt : datetime):
    return dt.strftime("%d/%m/%Y %I:%M")

r = q2(datetime.datetime.now())
print(r)

'''
Write a function that adds a specified number of days to the current date and returns the new date.
'''
from datetime import datetime, timedelta
def q3(d):
    return datetime.now().date()+timedelta(days=d)
r = q3(10)
print(r)

'''
Using the datetime module, write a function that returns the current date and time in the format 'YYYY-MM-DD HH:MM
'''
import datetime
def q4(dt : datetime):
    return dt.strftime("%Y-%m-%d %I:%M")

r = q4(datetime.datetime.now())
print(r)