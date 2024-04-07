from pathlib import Path

user_input = input("Enter file name: ")

try:
    path = Path(user_input)
    contents = path.read_text(encoding="UTF-8") 
    print(contents)
except FileNotFoundError:
    print(f"The file {user_input} is not found")
