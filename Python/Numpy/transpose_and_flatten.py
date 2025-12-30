'''Task
You are given a NXM integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.
Input Format
The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of M columns.
Output Format
First, print the transpose array and then print the flatten.
Sample Input
2 2
1 2
3 4
Sample Output
[[1 3]
[2 4]]
[1 2 3 4]'''

import numpy

N, M = map(int, input().split())

arr =[]
for _ in range(N):
    arr.append(list(map(int, input().split())))
change_arr = numpy.array(arr)
print(change_arr.T)
print(change_arr.flatten())