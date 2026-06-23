"""
151. Reverse Words in a String 
Given a input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by atleast one space.
Return a string of the words in reverse order concatenated by a single space.

Note: That s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces. 

Example1: 
Input: s = "the sky is blue"
Output: "blue is sky the"

Input: "  hello world  "
Output: "world hello"


"""
import collections 

def reverse_word(str1):
    """Method 1: using inbuilt functions"""
    str1_ls = str1.strip().split(' ')
    str1_ls = [word for word in str1_ls if word != '']
    reversed_str1_ls = list(reversed(str1_ls))
    return ' '.join(reversed_str1_ls)

def reverse_word2(str1):
    """ Method 2: without using built in functions"""
    str1_ls = list(str1)
    left, right = 0, len(str1_ls) 
    output_ls = []
    while left < right:
        if str1_ls[left] == ' ':
            left += 1
            continue
        for j in range(left, right):
            if str1_ls[j] == ' ':
                # left += 1
                break 
        output_ls.insert(0, ''.join(str1_ls[left:j]))
        left = j 
    print(output_ls)


def reverse_word3(str1):
    string_builder = collections.deque() 
    start = -1 
    i = 0 
    while i < len(str1):
        if str1[i] != " ":
            start = i 
            while i < len(str1) and str1[i] != ' ':
                i+= 1
            string_builder.appendleft(str1[start: i])
            i -= 1
        i += 1

    return " ".join(string_builder)


def reverse_word4(str1):
    """' '.join(list(reversed([word for word in str1.split(' ') if word.isalnum()])))"""
    result = []
    n = len(str1) 
    i = 0
    while i < n:
        # Ignoring blank spaces
        while i < n and str1[i] == ' ': 
            i += 1
        if i >= n:
            break
        # finding the leading non-blank characters
        j = i + 1 
        while j < n and str1[j] != ' ': # __blue__
            j += 1 
        result.insert(0, str1[i:j])
        i = j + 1
    print(result)

if __name__ == '__main__':
    str1=  input("Enter the string to do reversal word: \n")
    output_str = reverse_word4(str1)
    # print(f"the string {str1} reversed is {output_str}")
    print(output_str)