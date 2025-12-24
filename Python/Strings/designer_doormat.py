'''Input Format
A single line containing the space separated values of N and M.
Constraints
5 < N < 101
15 < M < 303
Output Format
Output the design pattern.
Sample Input
9 27
Sample Output
Refer Hackerrank: https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

# Top part
for i in range(n // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(m, '-'))

# Middle line
print("WELCOME".center(m, '-'))

# Bottom part
for i in range(n // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(m, '-'))
