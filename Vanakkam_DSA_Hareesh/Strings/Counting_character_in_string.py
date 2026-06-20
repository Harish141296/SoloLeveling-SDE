"""
Counting character in the given string
"""

def count_Character(str1: str, target: str) -> int:
    """count the character in the given string"""
    counter = 0 
    for char in str1:
        if char == target:
            counter += 1

    # inbuilt method : 
    print(f"Count the occurance of the given string with inbuilt count() : {str1.count(target)}")
    return counter

if __name__== '__main__':
    str1 = input("Enter the String: \n")
    target = input("Enter the character that you want to count: \n")
    occured = count_Character(str1, target)
    print(f"The character {target} Occured {occured}* times in {str1}")

    print('success.')