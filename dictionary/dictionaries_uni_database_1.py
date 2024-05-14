
def insert_degree_program(dict, program):
 if program in dict:
  print(f"{program} is already in the database")
 else:
    dict[program] = []
    return dict

def insert_course(dict, program, course):
  if program not in dict:
    print(f"Unknown degree program: {program}")
  elif course in dict[program]:
    print(f"{course[0]} is already in the database")
  else:
    dict[program].append(course)
  return dict

def print_degree_program(dict, program):
  total_courses = len(dict[program])
  print(f"{program} ({total_courses} courses)")
  
  total_credits = 0
  for course in dict[program]:
    course_name, credits = course
    total_credits += credits
    print(f"  {course_name}, {credits} credits")
  print(f"  Total credits: {total_credits}")

def main():
 db = {}
 insert_degree_program(db, "ITBBA")
 insert_degree_program(db, "EXPER")
 insert_course(db, "ITBBA", ("Python Programming", 5))
 insert_course(db, "ITBBA", ("Time Management", 3))
 insert_course(db, "EXPER", ("Creative Hospitality and Tourism", 5))
 insert_course(db, "EXPER", ("Managing Dynamic Restaurant Business", 10))
 print_degree_program(db, "ITBBA")
 print_degree_program(db, "EXPER")
 
main()
