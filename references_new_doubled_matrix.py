from copy import deepcopy

def new_doubled_matrix(list):
 new_list = deepcopy(list)
 for index in range(len(new_list)):
  for i in range(len(new_list[index])):
   new_list[index][i] *=2
 return new_list
 

def main():
 m1 = [[1, 2, 3], [4, 5, 6]]
 m2 = new_doubled_matrix(m1)
 print(m1)
 print(m2)
main()
