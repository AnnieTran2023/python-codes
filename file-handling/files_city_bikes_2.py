from pathlib import Path

def load_file(file_name):
    path = Path(__file__).resolve().parent # 1. Get the current script's folder path
    path = path / file_name # 2. Append the file name to the folder path
    try:
        contents = path.read_text(encoding="UTF-8")  # Read the file content as a single string
        lines = contents.splitlines()  # Split the string into a list of strings
        return lines
    except FileNotFoundError:
        print(f"The file {file_name} is not found")
        return []
    

def show_max_departures (list):

    stations = {}
    for line in list[1:]:
        fields = line.split(",")
        if len(fields) >= 8:
            if fields[3] not in stations:
                stations[fields[3]] = 1
            else:
                stations[fields[3]] +=1
    
    max_count = 0
    max_departure = []
	
    for departure, count in stations.items():
        if count > max_count:
            max_count = count
            max_departure = [departure]
        elif count == max_count:
            max_departure.append(departure)
    
    max_departure.sort()

    print("\nMaximum number of departures from a bike station: ")
    for departure in max_departure:
        print(f"{departure} ({max_count} departures)")

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
    list = load_file(file)
    show_statistics(list)
    show_max_departures (list)

main()
