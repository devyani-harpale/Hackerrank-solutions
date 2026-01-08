'''Task
You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:
&& → and
||→ or
Both && and || should have a space"" on both sides.
Input Format
The first line contains the integer, N.
The next N lines each contain a line of the text.
Constraints
0 < N < 100
Neither && nor || occur in the start or end of each line.
Output Format
Output the modified text.
Sample Input
11 b = input(); a = 1
if a + b > 0 && ab < 0: start() elif a*b>1 theta|| a / b < 1 ; stop() print set(list(a)) | set(list(b)) #Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those || which have space on both sides.
Sample Output
a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.   '''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

for _ in range(N):
    line = input()
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    print(line)
    