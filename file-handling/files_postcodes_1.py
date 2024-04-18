from pathlib import Path

def load_data (file_name):
    path = Path(__file__).resolve().parent
    path = path / file_name

    post_office = {}
    try:
        contents = path.read_text(encoding="UTF-8") 
        lines = contents.splitlines() 
        print(f"{len(lines)} rows")
        for line in lines[1:]:
            fields = line.split(";")
            if len(fields) >= 3:
                post_office[fields[0]] = [fields[1], fields[2]]

        return post_office

    except FileNotFoundError:
        return None

def main():
    file = input("Enter postcode file name: ")
    result = load_data(file)
    if result == None:
        print(f"\nThe file {file} is not found")
    else:
        postcode = int(input("\nEnter postcode: "))
        is_found = False
        for code in result:
            if int(code) == postcode:
                is_found = True
                print(f"{code} {result[code][0]}")
                print(f"{code} {result[code][1]}")
        if is_found == False:
            print("Unknown postcode")

main()
