'''You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
Www.HackerRank.com www.hACKER ANK.COM
Pythonist 2 PYTHONIST 2
Function Description
Complete the swap_case function in the editor below.
swap_case has the following parameters:
string s: the string to modify
Returns
string: the modified string
Input Format
A single line containing a string 8.
Constraints
0 < len(s) <= 1000
Sample Input O
HackerRank.com presents "Pythonist 2".
Sample Output O
HACKERrANK.COM PRESENTS "PYTHONIST 2".'''

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)