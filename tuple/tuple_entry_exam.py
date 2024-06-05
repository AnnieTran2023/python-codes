def grade_exam(list, score):
    passed_students = []
    for index in range(len(list)):
        if list[index][1] >= score:
            passed_students.append(list[index])
    return passed_students

def main():
    applicants = [("Ann", 30), ("Jack", 25), ("Jill", 40)]
    passed_applicants = grade_exam(applicants, 30)
    print("Entry exam passed")
    for name, points in passed_applicants:
        print(f"{name}, {points} points")

if __name__ == "__main__":
    main()
