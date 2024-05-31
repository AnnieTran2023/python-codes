def length_of_longest_substring(s):
    char_index = {}
    max_length = start = 0
    
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        
        char_index[char] = i

    return max_length

if __name__ == "__main__":
    input_string = "abcabcbb"
    result = length_of_longest_substring(input_string)
    print("Length of the longest substring without repeating characters:", result)
