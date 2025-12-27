'''Task
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marke, class and name.
Your task is to help Dr. Wesley calculate the average marks of the students
Average = Sum of all marks Total Students
Nolic
1. Columne can be in any ander. IDs, marks, class and name can be written in any onder in the spreadshoot
2. Column names are ID, MARKS, CLASS and NAUKE (The apolling and case type of these names won't change)
Input Format
The first line contains an integer N. the total number of students.
The second line contains the names of the columns in any order.
The next V lines contains the marks. IDs. name and class, under their respective column names.
Constraints
0 < N < 100
Output Format
Print the average marks of the list corrected to 2 decimal places.
Sample Input
TESTCASE OF
5
ID
MARKS
NAME
CLASS
1
97
Raymond
7
2
58
Steven
3
91
Adrian 9
4
72
Stewart
5
5
88
Peter
6
TESTCASE 02
5
MARKS
CLASS
NAME
ID
92
2
Calum
1
82
5
Scott
2
94
2
Jason
3
55
Glenn
4
82
2
Fergus 5
Sample Output
TESTCASE 01
78.00
TESTCASE 02
81.08'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N = int(input())
feilds = input().split()
total_marks = 0
avg = 0
for student in range(N):
    student_inp = namedtuple('student_inp', feilds)
    MARKS, CLASS, NAME, ID = input().split()
    student = student_inp(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
avg = total_marks / N
print(f"{avg:.2f}")
