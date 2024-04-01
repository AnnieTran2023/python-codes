members = {"John": "software developer", "Ann": "project manager", "Susan": "software developer", "Jill": "lead developer"}

search_name = input("Enter name (quit ends): ")

while search_name != "quit":

    role = input("Enter role: ")

    is_found = False

    for name in members:
        if name == search_name:
            members[name] = role
            is_found = True
    
    if is_found == False:
        members[search_name] = role
    
    search_name = input("\nEnter name (quit ends): ")

sorted_dict = dict(sorted(members.items()))
print()
for name, role in sorted_dict.items():
    print(f"{name:7s} {role:>8s}")
