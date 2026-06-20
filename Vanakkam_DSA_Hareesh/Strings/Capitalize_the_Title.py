"""
leetcode.com/problems/capitalize-the-title/description/?envType=problem-list-v2&envid=string
You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. 
Capitalize the string by changing the capitalization of each word such that: 
* If a length of the word is 1 or 2 letters, change all the letters to lowercase.
* Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title.


Example1: 
input: title = "capiTalIze tHe titLe"
output: "Capitalize The Title"
Example2:
input: title = "First leTTeR oF EACH Word"
output: "First Letter of Each Word"

"""

class Solution:
    def __init__(self, str1):
        self.str1 = str1 

    def _capitalize_string(self):
    
        new_capitalized_str = []
        ls_str1 = self.str1.split(' ')
        for word in ls_str1:
            if len(word) < 3:
                new_capitalized_str.append(word.lower())
            else:
                # with using the inbuilt function title() 
                # word = word.title()
                # new_capitalized_str.append(word)
                # without using the input built function 

                word = word.lower()
                word = word[0].upper() + word[1:].lower()
                new_capitalized_str.append(word)

        return " ".join(new_capitalized_str)





if __name__ == '__main__':
    str1 = input("Enter the string to Capitalize: ")
    sol = Solution(str1)
    str2 = sol._capitalize_string()
    print(f"Capitalized String: {str2}")