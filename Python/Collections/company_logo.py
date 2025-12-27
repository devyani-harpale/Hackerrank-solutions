'''A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names
and logos based on this condition. Given a string a, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,
and would have it's logo with the letters.
Input Format
A single line of input containing the string S.
Constraints
3 < le*pi(S) <= 10 ^ 4
S has at least 3 distinct characters
Output Format
Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
Sample Input O
sabbbcode
Sample Output 0
b3
2
2
Explanation O
Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.
Note: The string S has at least 3 distinct characters.'''

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    s = sorted(s)
    letter_count = {}
    for letter in s:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    letters_sorted = sorted(letter_count.items(), key = lambda x:(-x[1], x[0]))
    
    for key,value in letters_sorted[:3]:
        print(key,value)