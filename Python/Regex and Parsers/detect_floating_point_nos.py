'''You are given a string N.
Your task is to verify that N is a floating point number.
In this task, a valid float number must satisfy all of the following requirements:
symbol. Number can start with +, or
For example:
+4.50
-1.0
1.5
1-7
+4
X-+4.5
Number must contain at least
decimal value.
For example:
X12.
12.0
> Number must have exactly one. symbol.
> Number must not give any exceptions when converted using float(N).
Input Format
The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.
Constraints
0 < T < 10
Output Format
Output True or False for each test case.
Sample Input O
4
4.000
-1.00
+4.54
Some RandomStuff
Sample Output 0
False
True
True
False'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())
for _ in range(T):
    N = input().strip()
    print(bool(re.match(r'^[+-]?\d*\.\d+$', N)))