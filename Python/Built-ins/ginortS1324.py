'''Your task is to sort the string S' in the following manner:
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format
A single line of input contains the string S.
Constraints
0 < lem(S) < 1000
Output Format
Output the sorted string S.
Sample Input
Sorting1234
Sample Output
ginort$1324'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
S = input()

sorted_string =  sorted(S, key= lambda x: (
        x.isdigit() and int(x) % 2 == 0,
        x.isdigit() and int(x) % 2 != 0,
        x.isupper(),
        x))
print(''.join(sorted_string))