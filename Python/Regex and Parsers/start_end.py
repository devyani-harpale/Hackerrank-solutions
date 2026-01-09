'''Task
You are given a string S.
Your task is to find the indices of the start and end of string k in S.
Input Format
The first line contains the string S.
The second line contains the string k.
Constraints
0 < len(S) < 100
0 < len(k) < len(S)
Output Format
Print the tuple in this format: (start_index, end_index).
If no match is found, print (-1, -1).
Sample Input
aa
Sample Output
(0, 1)
(1, 2)
(4,5)'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
k = input()

matches = list(re.finditer(rf'(?=({k}))', s))

if matches:
    for m in matches:
        print((m.start(1), m.start(1) + len(k) - 1))
else:
    print((-1, -1))