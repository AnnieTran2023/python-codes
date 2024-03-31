members = {"John": "software developer", "Ann": "project manager", "Susan": "software developer", "Jill": "lead developer"}

search = input("Enter name(quit ends): ")

while search != "quit":

    is_found = False
    for key in members:
        if search == key:
            print(f"{search} is a {members[key]}")
            is_found = True
    if is_found == False:
        print(f"{search} is not in the team ")

    search = input("\nEnter name (quit ends): ")
