'''Your task is to determine the winner of the game and their score.
Function Description
Complete the minion_game in the editor below.
minion_game has the following parameters:
string string: the string to analyze
Prints
string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format
A single line of input containing the string S.
Note: The string S will contain only uppercase letters: [A-Z].
Constraints
0 < len(S) <= 10 ^ 6
Sample Input
BANANA
Sample Output
Stuart 12
Note:
Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.'''

def minion_game(string):
    # your code goes here
    Stuart = 0
    Kevin = 0
    vowels = "AEIOU"
    n = len(s)
    
    for i in range(n):
        if s[i] in vowels:
            Kevin += n - i
        else:
            Stuart += n - i
    if Kevin > Stuart:
        print("Kevin",Kevin)
    elif Stuart > Kevin:
        print("Stuart",Stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)