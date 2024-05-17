start_time = int(input("Enter start time: "))
length = int(input("Enter length: "))
wage = float(input("Enter wage: "))

end_time = start_time + length
display_end_time = 0
if end_time <= 24:
    display_end_time = end_time
else:
    display_end_time = end_time - 24

print(f"\nThe work shift ends at {display_end_time:02d}:00")

paid = 0
if length <= 8:
   paid = length * wage
else:
    overtime = length - 8
    paid = (8 * wage) + (overtime * wage * 2)
print(f"The earnings are {paid:.2f} euros")
