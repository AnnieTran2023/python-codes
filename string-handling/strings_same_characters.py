def strings_same_characters():

    str1 = input("Enter first string: ").lower()
    str2 = input("Enter second string: ").lower()

    str1_not_spaces = ''.join(str1.split())
    str2_not_spaces = ''.join(str2.split())

    if set(str1_not_spaces) == set(str2_not_spaces) and len(str1_not_spaces) == len(str2_not_spaces):
        print("Same characters")
    else:
        print("Different characters")


strings_same_characters()
