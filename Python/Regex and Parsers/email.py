'''Output Format
Print the space-separated name and email address pairs containing valid email addresses only. Each pair must be printed on
a new line in the following format:
name <user@email.com>
You must print each valid email address in the same order as it was received as input.
Sample Input
2
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
Sample Output
DEXTER <dexter@hotmail.com>
Explanation
dexter@hotmail.com is a valid email address, so we print the name and email address pair received as input on a new line.
virus!@variable.:p is not a valid email address because the username contains an exclamation point (!) and the extension'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'^[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

for _ in range(int(input())):
    name, email = input().split()
    email = email[1:-1]  # remove < >

    if re.match(pattern, email):
        print(f"{name} <{email}>")
