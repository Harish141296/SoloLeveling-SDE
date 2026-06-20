"""
Check two strings identical or not
"""

def is_same_string(str1, str2):
    if len(str1) != len(str2):
        return False 
    for i in range(len(str1)):
        if str1[i].lower() != str2[i].lower():
            return False 
    return True 

if __name__ == '__main__':
    str1=  input("Enter the first string: \n")
    str2 = input("Enter the second string: \n")
    if is_same_string(str1, str2):
        print(f"The string {str1} and {str2} are identical ")
    else:
        print(f"The string {str1} and {str2} are not identical ")

    print("Success.")
