'''Task
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu eamed.
Input Format
The first line contains X, the number of shoes
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and, the price of the shoe.
Constraints
0 < X < 10 ^ 2
0 < N <= 10 ^ 2
20 < x_{i} < 100
2 shoe size < 20
Output Format
Print the amount of money esmed by Roghu.
Sample Input
16
234568 7 6 5 18
6
655
6.45
6.55
449
18 68
18 50
Sample Output
200'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
shoe_sizes = list(map(int, input().split(' ')))
shoe_counter = Counter(shoe_sizes)
n = int(input())
total_earnings = 0

for _ in range(n):
    cust_shoe_size, price = map(int, input().split())
    if shoe_counter[cust_shoe_size] > 0:
        total_earnings += price
        shoe_counter[cust_shoe_size] -= 1
        
print(total_earnings)
