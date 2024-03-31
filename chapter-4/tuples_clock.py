def roll_forward(tup_time, hours, minutes):
    
    x,y = tup_time
    
    y = y + minutes
    x = x + hours
 
    if y > 59:
        x = x + (y // 60)
        y = y % 60
    
    
    if x > 23:
        x = x % 24

    return (x,y)

def main():

    tup_time = (00,00)

    print(f"The current time is {tup_time[0]:02d}:{tup_time[1]:02d}")

    hours = int(input("Enter hours to add: "))

    while hours >= 0:
        minutes = int(input("Enter minutes to add: "))
        tup_time = roll_forward(tup_time, hours, minutes)
        print(f"{tup_time[0]:02d}:{tup_time[1]:02d}")
        hours = int(input("Enter hours to add: "))
    
main()




