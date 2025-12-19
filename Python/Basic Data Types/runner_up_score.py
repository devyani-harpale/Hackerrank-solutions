'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
Constraints
2 <= n <= 10
- 100 <= A[i] <= 100
Output Format
Print the runner-up score.
Sample Input O
5
23665
Sample Output O
5
Explanation O
Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    max_score = float('-inf')
    second_max_score = float('-inf')
    for i in arr:
        if i > max_score:
            second_max_score = max_score
            max_score = i
        elif  max_score > i > second_max_score:
            second_max_score = i
print(second_max_score)
