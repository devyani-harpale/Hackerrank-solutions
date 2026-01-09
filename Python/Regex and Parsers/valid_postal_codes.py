'''Your task is to provide two regular expressions regex_integer_in_range and
regex_alternating_repetitive_digit_pair. Where:
regex_integer_in_range should match only integers range from 100000 to 999999 inclusive
regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.
Both these regular expressions will be used by the provided code template to check if the input string P is a valid postal code
using the following expression:
(bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
Input Format
Locked stub code in the editor reads a single string denoting P from stdin and uses provided expression and your regular expressions to validate if P is a valid postal code.
Output Format
You are not responsible for printing anything to stdout. Locked stub code in the editor does that.
Sample Input O
110000
Sample Output O
False'''
regex_integer_in_range = r"^[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)