'''Task
You are given two integer arrays of size NXP and MXP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis
0.
Input Format
The first line contains space separated integers N. M and P.
The next V lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.
Output Format
Print the concatenated array of size (N+M)x P.
Sample Input
4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4
Sample Output
[[1 2]
[1 2]
[1 2]
[1 2]
[3 4]
[3 4]
[3 4]]'''
import numpy

N, M, P = map(int, input().split())

arr1 = numpy.array([list(map(int, input().split())) for _ in range(N)])

arr2 = numpy.array([list(map(int, input().split())) for _ in range(M)])

result = numpy.concatenate((arr1, arr2), axis=0)

print(result)