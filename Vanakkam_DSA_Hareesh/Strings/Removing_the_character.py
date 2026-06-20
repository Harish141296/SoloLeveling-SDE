"""
Remove the given character from the string 
"""

def remove_character(str1, replaceable_str):
    print(f"Using Inbuilt method :{str1.replace(replaceable_str, '')}") 
    new_str1 = ''
    for char in str1:
        if replaceable_str== char:
            continue 
        new_str1 += char 
    return new_str1 

if __name__ == '__main__':
    str1 = input("Enter the string: ")
    replaceable_str = input("Enter the string that want to be removed: ")
    new_str1 = remove_character(str1, replaceable_str)
    print(f"New String {new_str1} after removing {replaceable_str} from {str1}")

    print("success.")