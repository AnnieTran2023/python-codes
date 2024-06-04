list = []

for i in range(7):
    number = int(input("Enter an integer: "))
    list.append(number)

new_list = []

for i in range (1,8,2):
    if i == 7:
        new_list.append(list[i-1])
    elif i != 7:
        new_list.append(list[i])
        new_list.append(list[i-1])
        
print(new_list)

