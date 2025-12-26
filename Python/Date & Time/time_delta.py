'''When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that
a user can see on his newsfeed in the following format:
Day dd Mon yyyy hh:mm:ss +XXXX
Here +xxxxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
Input Format
The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t₁ and time t2.
Constraints
Input contains only valid timestamps
year < 3000.
Output Format
Print the absolute difference (t112) in seconds.
Sample Input O
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36-0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36-0000
Sample Output O
25200 88200
Explanation O
In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is 7 x 3600 seconds or 25200 seconds.
Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 24 x 3600+30×6088200'''

#!/bin/python3
from datetime import datetime
import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    format_str = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, format_str)
    dt2 = datetime.strptime(t2, format_str)
    return abs(int((dt1 - dt2).total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()
