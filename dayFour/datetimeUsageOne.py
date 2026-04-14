'''
    Intro to datetime module
'''
import datetime

dateVar = datetime.date.today()
print(dateVar)
print(dateVar.year)
print(dateVar.month)
print(dateVar.day)

timeVar = datetime.time(16,44,59)
print(timeVar)

#date and time 
dateTimeVar = datetime.datetime.now()
print(dateTimeVar)

dtVar = datetime.datetime(2026, 4, 14, 16, 44, 50)
print(dtVar)

#timedelta --> time differences
diff = datetime.timedelta(days=3, hours=4)
print(diff)

dateOne = datetime.date.today()
dateTwo = datetime.date(2027,2,13)
print(dateTwo - dateOne)

#date formatting using strftime function
#14-Apr-2026

print(dateTimeVar.strftime("%d-%B-%y %H:%M:%S"))