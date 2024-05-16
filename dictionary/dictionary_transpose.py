def transpose_dictionary(dict):
 for key, value in dict.copy().items():
  dict[value] = key
  dict.pop(key)
 return dict

def main():
 vocabulary = {"cat": "kissa", "dog": "koira", "bird": "lintu"}
 print(vocabulary)
 transpose_dictionary(vocabulary)
 print(vocabulary)

main()
