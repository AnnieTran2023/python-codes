from datetime import date
from calendar import monthrange

def print_month_calendar(year, month): 
    month_names = ["", "January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]
    print(f" > {month_names[month]} {year} <")

    my_date = date(year,month,1)
    day_of_week = my_date.weekday() + 1
    days_in_the_month = monthrange(year, month)[1]
	
    print(" Mon Tue Wed Thu Fri Sat Sun")

    #first-row
    for i in range(1,9-day_of_week):
        if i == 1 and 8-day_of_week == 1:
            print(f"{i:{day_of_week*4}d}")
        elif i == 1:
            print(f"{i:{day_of_week*4}d}", end="")
        elif i == 8-day_of_week:
            print(f"{i:4d}")
        else:
            print(f"{i:4d}", end ="")

    #other-rows
    count = 1
    for i in range(9-day_of_week, days_in_the_month+1):
        if count % 7 == 0:
            print(f"{i:4d}")
        elif i == days_in_the_month:
            print(f"{i:4d}")
        else: 
            print(f"{i:4d}", end ="")
        count +=1


def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    print()
    print_month_calendar(year, month)

main()
