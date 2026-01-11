"""Question 2: Monotonic Array - An array is Monotonic if it is either monotone increasing or monotone decreasing. An array is monotone increasing if all its elements from left to right are non-decreasing. An array is monotone decreasing if all its elements from left to right are non-increasing. Given an integer array return true if the given array is monotonic, or false otherwise. 

Input: [1,2,3,7]

Expected Output: True

Input: [3, 2, 1, -1]

Expected Output: False 

"""
print("Monotonic Array Script Execution Begins.")
def monotonic_array(arr):
    n = len(arr)
    if n in [0, 1]: return True 
    first, last = arr[0], arr[n-1]
    if first > last: 
        # MD or array is not monotonic
        for k in range(n - 1):
            if arr[k] < arr[k+1]: 
                return False
        return True
        # for k in range(n -1 ):
        #     pass 
    elif first == last:
        # M - all values are equal or array is not monotonic

        for k in range(n - 1):
            if arr[k] != arr[k+1]: 
                return False
        return True
    
    elif first < last:
        for k in range(n - 1):
            if arr[k] > arr[k+1]: 
                return False
        return True
    else:
        return False
         

input_arr = [1,2,2] # MI
print(monotonic_array(input_arr)) 
input_arr = [2,2,2] # ME
print(monotonic_array(input_arr)) 
input_arr = [2,2,1] # MD
print(monotonic_array(input_arr))
input_arr = [2,2,5,2] # MD
print(monotonic_array(input_arr))
print("Monotonic Array Script Execution Ends.")

