'''To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.
If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space for better readability.
Neo feels that there is no need to use 'if' conditions for decoding.
Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
Input Format
The first line contains space-separated integers N (rows) and M (columns) respectively.
The next N lines contain the row elements of the matrix script.
Constraints
0 < N, M < 100
Note: A 0 score will be awarded for using 'i f' conditions in your code.
Output Format
Print the decoded matrix script.
Sample Input O
73
Tsi
h%x
i#
SM
$a
#t%
ir!
Sample Output O
This is Matrix# %!'''
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded = ''.join(matrix[i][j] for j in range(m) for i in range(n))
decoded = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded)

print(decoded)