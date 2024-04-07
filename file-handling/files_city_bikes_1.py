from pathlib import Path

def load_file(file_name):
    path = Path(__file__).resolve().parent
    path = path / file_name 
    try:
        contents = path.read_text(encoding="UTF-8")
        lines = contents.splitlines()
        return lines
    except FileNotFoundError:
        print(f"\nThe file {file_name} is not found")
        return []

    return lines

def show_statistics (data_list):

    if data_list == []:
        return []

    total_m = 0
    total_duration = 0
    for line in data_list[1:]:
        fields = line.split(",")
        if len(fields) >= 8:  
            total_m += int(fields[6])
            total_duration += int(fields[7])

    average_distance = total_m / 1000 / (len(data_list)-1)
    average_duration = total_duration / (len(data_list)-1) / 60
    print(f"\n{total_m//1000} kilometers on {len(data_list)-1} bike rides")
    print(f"Average distance: {average_distance:.1f} kilometers")
    print(f"Average duration: {average_duration:.0f} minutes")

def main():
    file = input("Enter file name: ")
    show_statistics(load_file(file))

main()
