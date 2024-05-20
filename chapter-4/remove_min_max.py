def remove_min_max(list):
    if len(list) == 0:
        return
    elif len(list) == 1:
        list.pop(0)
        return 
    else:
        list.sort()
        list.pop(0)
        list.pop(len(list)-1)

def main():
    a = [3, 1, 4, 1, 5]
    remove_min_max(a)
    print(a)
    b = [42]
    remove_min_max(b)
    print(b)

if __name__ == "__main__":
    main()
