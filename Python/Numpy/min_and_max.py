'''Task
You are given a 2-D array with dimensions NXM.
Your task is to perform the min function over axis 1 and then find the max of that.
Input Format
The first line of input contains the space separated values of N and M.
The next N lines contains M space separated integers.
Output Format
Compute the min along axis 1 and then print the max of that result.
Sample Input
42
25
37
13
40
Sample Output
3
Explanation
The min along axis 1 = [2,3,1,0] The max of [2, 3, 1, 0] = 3'''
import numpy

N, M = map(int, input().split())

my_array = numpy.array([list(map(int, input().split())) for _ in range(N)])
    
min_result = numpy.min(my_array, axis=1)
print(numpy.max(min_result))