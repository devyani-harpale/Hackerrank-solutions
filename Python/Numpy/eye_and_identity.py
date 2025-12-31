'''Task
Your task is to print an array of size NXM with its main diagonal elements as 1's and O's everywhere else.
Note
In order to get alignment correct, please insert the line numpy.set_printoptions (legacy='1.13') below the numpy
import.
Input Format
A single line containing the space separated values of N and M.
N denotes the rows.
M denotes the columns.
Output Format
Print the desired NXM array.
Sample Input
33
Sample Output
[[1. 0. 0.]
[0. 1. 0.]
[ 0. 0. 1.]]'''

import numpy
numpy.set_printoptions(legacy='1.13')

N, M = map(int, input().split())
print(numpy.eye(N, M))