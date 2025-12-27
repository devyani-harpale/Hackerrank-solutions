'''There is a horizontal row of in cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cubeli] is on top of cube[j] then
sideLength[j]> side Length[i]
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.
Example
blocks [1,2,3,8,7]
Result: No
After choosing the rightmost element, 7, choose the leftmost element, 1. After than, the choices are 2 and 8. These are both larger than the top block of size 1.
blocka [1,2,3,7,8]
Result: Yes
Choose blockes from right to left in order to successfully stack the blocks.
Input Format
The first line contains a single integer T, the number of text cases.
For each test case, there are 2 lines
The first line of each test case contains n the number of cubes.
The second line contains space separated integers, denoting the sidelengths of each cube in that order.
Constraints
1 <= \mathcal{T} <= \mathfrak{b}
1 <= n <= 10 ^ 5
1 < side Length < 281
Output Format
For each test case, output a single line containing either Yes or No.
Sample Input
STDIN
2
6
Function
T = 2
blocks size n = 6
432134
blocks [4, 3, 2, 1, 3, 4]
3
blocks
size n = 3
132
blocks
[1, 3
Sample Output
Yes No
Explanation
In the first test case, pick in this order: left-4, right-4, left-3, right-3, left-2, right-1.
In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

def can_stack_cubes(blocks):
    left = 0
    right = len(blocks)-1
    current_top = float('inf')
    
    while left <= right:
        if blocks [left] >= blocks [right]:
            chosen_cube = blocks [left]
            left += 1
        else:
            chosen_cube = blocks[right]
            right -= 1
            
        if chosen_cube > current_top:
            return "No"
        
        current_top = chosen_cube
        
    return "Yes"
    
    
for _ in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))
    print(can_stack_cubes(blocks))
