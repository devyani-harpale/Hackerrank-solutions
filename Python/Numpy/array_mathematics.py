'''Task
You are given two integer arrays. A and B of dimensions NXM.
Your task is to perform the following operations:
1. Add (A + B)
2. Subtract (A - B)
3. Multiply (AB)
4. Integer Division (A/B)
5. Mod (A% B)
6. Power (A** B)
Note
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.
Input Format
The first line contains two space separated integers. N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B.
Output Format
Print the result of each operation in the given order under Task.
Sample Input
14
1234
5678
Sample Output
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]'''
import numpy

numpy.set_printoptions(legacy='1.13')

N, M =map(int, input().split())

A = numpy.array([list(map(int, input().split())) for _ in range(N)])
B = numpy.array([list(map(int, input().split())) for _ in range(N)])
    
print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A,B))
print(numpy.floor_divide(A,B))
print(numpy.mod(A,B))
print(numpy.power(A,B))