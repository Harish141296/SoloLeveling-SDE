"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if its a palindrome, or false otherwise. 

Example1: 
Input s="A man, a plan, a canal: Panama"
Output: true 
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

def valid_palindrome(str1):
    '''Method 1'''
    str1 = [char.lower() for char in list(str1) if char.isalnum()]
    rev_str1 = list(reversed(str1))
    _len = len(str1)
    for i in range(_len - 1):
        if str1[i] != rev_str1[i]:
            return False 
    return True 

def valid_palindrome2(str1):
    '''Method 2'''
    print("Method 2 is acting now.")
    str1 = [char.lower() for char in list(str1) if char.isalnum()]
    left, right = 0, len(str1)-1
    while left < right:
        if str1[left] != str1[right]:
            return False 
        left += 1 
        right -= 1
    return True 
if __name__ == '__main__':
    str1 = input("Enter the string to check whether the given number is palindrome or not:\n")
    if valid_palindrome(str1):
        print(f"Given string {str1} is a valid palindrome \n")
    else:
        print(f"Given string {str1} is not a valid palindrome\n")
    if valid_palindrome2(str1):
        print(f"Given string {str1} is a valid palindrome \n")
    else:
        print(f"Given string {str1} is not a valid palindrome\n")