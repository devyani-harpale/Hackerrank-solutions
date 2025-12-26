'''Task
You are given a date. Your task is to find what the day is on that date.
Input Format
A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
Constraints
2000 < year < 3000
Output Format
Output the correct day in capital letters.
Sample Input
08 05 2015
Sample Output
WEDNESDAY
Explanation
The day on August 5th 2015 was WEDNESDAY.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
M_M, D_D, Y_Y_Y_Y = map(int, input().split())
day_num = calendar.weekday(year=Y_Y_Y_Y,month=M_M,day=D_D)
print(calendar.day_name[day_num].upper())