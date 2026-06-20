"""
Concatinating two string 
"""

def _concatinator(str1, str2):
    # without storing
    print(f"{str1} {str2}")
    # with '+' operator 
    new_word = str1 + " " + str2 
    print(f"Plus operator concatination: {new_word}")
    # Using join method: 
    new_word = ' '.join([str1, str2])
    print(f"using Join function: {new_word}")

if __name__ == '__main__':
    str1=  input("Enter the first string: \n")
    str2 = input("Enter the second string: \n")
    _concatinator(str1, str2)
    print("Success.")