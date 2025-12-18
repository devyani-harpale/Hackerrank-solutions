'''Task
Given an integer, n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Input Format
A single line containing a positive integer, n.
Constraints
1 <= n <= 100
Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.
Sample Input O
3
Sample Output O
Weird'''

import math
import os
import random
import re
import sys

n = int(input())
max_val = 100
min_val = 1
if n >= min_val and n <= max_val:
    if n % 2 == 0 and n in range(2, 5):
        print("Not Wierd")
    elif n % 2 == 0 and n in range(6, 20):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
    elif n % 2 !=0:
        print("Weird")