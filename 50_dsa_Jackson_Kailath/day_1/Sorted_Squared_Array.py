"""
Question 1: Sorted Squared Array - You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each numbers SORTED in ascending order.

Input: [-3, 1, 2, 7]

Expected Output: [1, 4, 9, 49]


"""
print("Sorted Squared Array Script Execution Begins.")
def sorted_squared(arr):
    """
    Converts array into squared array.
    
    :param arr: any integers
    """
    len_array = len(arr)
    res = [0] * len_array
    for i in range(len_array):
        res[i] = arr[i] ** 2 
    res.sort()
    return res 

input_arr = [-3, 1, 2, 4, 5, 20, 93]
# brute force method 
res = sorted_squared(input_arr) 
print(res) 

"""
brute force method takes:
time: O(n log n)
space: O(n)
"""

def sorted_square_optimized(arr):
    len_arr = len(arr) 
    left, right = 0, len_arr - 1 
    res = [0] * len_arr 

    for k in reversed(range(len_arr)):
        if arr[left] ** 2 > arr[right]**2:
            res[k] = arr[left] ** 2 
            left += 1 
        else:
            res[k] = arr[right] ** 2 
            right -= 1
    return res 


res = sorted_square_optimized(input_arr) 
print(res) 

print("Sorted Squared Array Script Execution Ends.")


