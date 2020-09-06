def count_substring(string, sub_string):
    count = 0
    i = 0
    sub_string_len = len(sub_string)

    while (i < len(string)):

        if sub_string == string[i:sub_string_len]:
            count += 1

        i += 1
        sub_string_len += 1

    print(count)
    return count

count_substring("abcdcd","cd")
