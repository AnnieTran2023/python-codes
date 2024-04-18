from pathlib import Path

def load_data (file_name):
    path = Path(__file__).resolve().parent
    path = path / file_name

    post_office = {}
    try:
        contents = path.read_text(encoding="UTF-8") 
        lines = contents.splitlines() 

        for line in lines[1:]:
            fields = line.split(";")
            if len(fields) >= 3:
                post_office[fields[0]] = [fields[1], fields[2]]

        return post_office

    except FileNotFoundError:
        return None

def main():
    dictionary = load_data("postcodes.csv")
    if dictionary == None:
        print(f"\nThe file postcodes.csv is not found")
    else:
        place = input("\nEnter place name: ").upper()
        is_found = False
        print()
        for postcode, postoffice in dictionary.items():
            if place in postoffice:
                is_found = True
                print(f"{postcode} {place}")

        if is_found == False:
            print("No postoffice found")

main()
