"""
ASCII - American Standard Code for Information Interchange
' ' - 32 
'a' - 97 
'z' - 122 
'A' - 65 
'Z' - 90

Hint: we will use '>' to check which is bigger
"""

"""
import java.utils.Arrays;
public class Main
{
public static void main(string[] args){
string str = "cabfed";
char[] chars = str.toCharArray():
Arrays.sort(chars);
string sortedStr = new String(chars);
System.out.println(sortedStr);
}
}
"""
def sortedstr(input_str):
    print(f"Before sorting: {input_str}")
    # list_str = [char for char in input_str]
    # sorted_str = ''.join(sorted(list_str))
    sorted_str = ''.join(sorted(input_str))
    return sorted_str

def bubble_sort_str(input_str):
    chars = list(input_str)
    char_length = len(chars)

    # Bubble sort algorithm 
    for i in range(char_length - 1):
        for j in range(char_length - i - 1):
            if chars[j] > chars[j + 1]:
                # Swap 
                chars[j], chars[j + 1] = chars[j + 1], chars[j] 
    
    return ''.join(chars) # converts list back to string 

if __name__ == '__main__':
    input_str=  input("Enter the string to sort: \n")
    new_sorted_str = sortedstr(input_str)
    print(f"After sorting: {new_sorted_str}")
    new_sorted_str_bs = bubble_sort_str(input_str)
    print(f"After sorting using Bubble sort: {new_sorted_str}")

    print("Success.")

