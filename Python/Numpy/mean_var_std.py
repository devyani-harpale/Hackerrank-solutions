'''Task
You are given a 2-D array of size NXM.
Your task is to find:
1. The mean along axis 1
2. The var along axis 0
3. The std along axis None
Input Format
The first line contains the space separated values of N and M.
The next N lines contains M space separated integers.
Output Format
First, print the mean.
Second, print the var.
Third, print the std.
Sample Input
22
12
34
Sample Output
[1.5 3.5]
[1. 1.]
1.11803398875'''
import numpy
N, M = map(int, input().split())

my_array = numpy.array([list(map(int, input().split())) for _ in range(N)])
    
print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))
print(round(numpy.std(my_array,axis=None),11))

