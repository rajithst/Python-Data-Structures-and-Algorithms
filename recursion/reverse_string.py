def reverse_string_helper(index, given_string):
    if given_string is None or index >= len(given_string):
        return
    reverse_string_helper(index + 1, given_string)
    print(given_string[index], end="")


reverse_string_helper(0, "rajith")


def reverse_string_of_array(array):
    def swap_letters(start, end, array):
        if start >= end:
            return
        array[start], array[end] = array[end], array[start]
        return swap_letters(start + 1, end - 1, array)

    swap_letters(0, len(array) - 1, array)


string_arr = list("rajith")
reverse_string_of_array(string_arr)
print(string_arr)