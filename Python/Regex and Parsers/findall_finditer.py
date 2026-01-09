'''Task
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+.-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.
Note:
Vowels are defined as: AEIOU and aeiou.
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.
Input Format
A single line of input containing string S.
Constraints
0 < len(S) < 100
Output Format
Print the matched substrings in their order of occurrence on separate lines.
If no match is found, print -1.
Sample Input
rabcdeefgyYhFjkIoomnpOeorteeeeet
Sample Output
ee
Ioo
Oeo
Explanation
ee is located between consonant d and f.
loo is located between consonant k and m.
Oeo is located between consonant p and r.'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()

matches = re.findall(r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])', S)

if matches:
    for m in matches:
        print(m)
else:
    print(-1)