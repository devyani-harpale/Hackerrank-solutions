'''Task
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
Input Format
A single line containing a string S.
Constraints
0 < len(S) < 1000
Output Format
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
Sample Input
qA2
Sample Output
True
True
True
True
True'''

if __name__ == '__main__':
    s = input()
    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False

    for ch in s:
        if ch.isalnum():
            has_alnum = True
        if ch.isalpha():
            has_alpha = True
        if ch.isdigit():
            has_digit = True
        if ch.islower():
            has_lower = True
        if ch.isupper():
            has_upper = True

    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)
        
