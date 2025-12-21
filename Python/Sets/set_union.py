'''Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.
Input Format
The first line contains an integer, 1n, the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b. the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.
Constraints
0 < Total number of students in college < 1000
Output Format
Output the total number of students who have at least one subscription.
Sample Input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3
11
21
55 6 8
Sample Output
13'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n_eng = int(input())
eng_set = set(map(int, input().split()))
b_french = int(input())
french_set = set(map(int, input().split()))
counter = 0
#atleast one which means one and more than one 
for i in list(eng_set.union(french_set)):
    counter += 1
print(counter)
