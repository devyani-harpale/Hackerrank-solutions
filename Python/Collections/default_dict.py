'''Example
Group A contains 'a', 'b', 'a' Group B contains 'a'. 'c'
For the first word in group B, 'a', it appears at positions 1 and 3 in group A. The second word, 'c', does not appear in group A
so print -1.
Expected output:
13
-1
Input Format
The first line contains integers, 2 and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.
Constraints
1 <= n <= 10000
1 <= m <= 100
1 length of each word in the input ≤ 100
Output Format
Output m lines.
The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.
Sample Input:
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
Sample Output:
1 2 4
3 5'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split(' '))
A = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    A[word].append(i)

for _ in range(m):
    word = input().strip()
    if word in A:
        print(*A[word])
    else:
        print(-1)