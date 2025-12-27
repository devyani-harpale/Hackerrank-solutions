'''Task
Perform append, pop, popleft and appendleft methods on an empty deque d.
Input Format
The first line contains an integer N. the number of operations.
The next N lines contains the space separated names of methods and their values.
Constraints
0 < N <= 100
Output Format
Print the space separated elements of deque d.
Sample Input
6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output
12'''

from collections import deque

N = int(input())
d = deque()

for _ in range(N):
    commands = input().split()
    
    if commands[0] == 'append':
        d.append(commands[1])
    
    if commands[0] == 'appendleft':
        d.appendleft(commands[1])
        
    if commands[0] == 'pop':
        d.pop()
        
    if commands[0] == 'popleft':
        d.popleft()
        
print(' '.join(d))