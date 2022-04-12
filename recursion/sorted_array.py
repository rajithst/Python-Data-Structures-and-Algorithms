def is_sorted(arr):
    # base case - if array has only one element or empty array,its sorted,return True
    if len(arr) == 1 or len(arr) == 0:
        return True
    # otherwise,compare first two element is sorted and recursively check rest of the array is sorted
    # if any point one of condition is false,return False
    if arr[0] < arr[1] and is_sorted(arr[1:]):
        return True
    return False


print(is_sorted([1, 2, 3, 41, 5]))
