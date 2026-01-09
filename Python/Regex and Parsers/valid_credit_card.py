'''You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
A valid credit card from ABCD Bank has the following characteristics:
It must start with a 4. 5 or 6.
It must contain exactly 16 digits.
It must only consist of digits (0-9).
It may have digits in groups of 4, separated by one hyphen "-".
It must NOT use any other separator like.. etc.
It must NOT have 4 or more consecutive repeated digits.
Examples:
Valid Credit Card Numbers
4253625879615786
4424424424442444
5122-2368-7954-3214
Invalid Credit Card Numbers
42536258796157867
4424444424442444
5122-2368-7954 3214
0525362587961578
#17 digits in card number Invalid
#Consecutive digits are repeating 4 or more times → Invalid
#Separators other than - are used → Invalid
#Contains non digit characters Invalid
#Doesn't start with 4, 5 or 6 Invalid
Input Format
The first line of input contains an integer N.
The next N lines contain credit card numbers.
Constraints
0 < N < 100
Output Format'''
import re

N = int(input())

pattern = re.compile(
    r'^(4|5|6)\d{3}(-?\d{4}){3}$'
)

for _ in range(N):
    card = input().strip()

    # Step 1: basic format validation
    if not pattern.match(card):
        print("Invalid")
        continue

    # Step 2: remove hyphens and check consecutive digits
    digits_only = card.replace('-', '')

    if re.search(r'(\d)\1{3,}', digits_only):
        print("Invalid")
    else:
        print("Valid")
