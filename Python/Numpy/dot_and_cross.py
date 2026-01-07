'''Task
You are given two arrays A and B. Both have dimensions of NXN.
Your task is to compute their matrix product.
Input Format
The first line contains the integer N.
The next N lines contains N space separated integers of array A.
The following N lines contains N space separated integers of array B.
Output Format
Print the matrix multiplication of A and B.
Sample Input
2
12
34
12
34
Sample Output
[[710]
[15 22]]'''
import numpy

N = int(input())

A = numpy.array([list(map(int, input().split())) for _ in range(N)])
B = numpy.array([list(map(int, input().split())) for _ in range(N)])

print(numpy.dot(A,B))