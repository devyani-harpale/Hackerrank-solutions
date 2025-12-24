'''Check Tutonal tab to know how to to solve
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.
Function Description
Complete the wrap function in the editor below.
wrap has the following parameters:
string string: a long string
int max_width: the width to wrap to
Returns
string: a single string with newline characters ('\n') where the breaks should be
Input Format
The first line contains a string, string.
The second line contains the width, maxwidth.
Constraints
0<len(string) < 1000
0< maxwidth < len(string)
Sample Input O
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output O
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ'''

import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    string = wrapper.fill(text=string)
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)