from datetime import date, time, datetime
#calling the day
#function of date class
today = date.today()
now = datetime.now()
print("Today's date is" , today)
print("\n Current date and time is" , now)

#Printing date's components
print("\n Date's components", today.year, today.month, today.day)