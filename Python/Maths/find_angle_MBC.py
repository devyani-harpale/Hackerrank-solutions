'''Input Format
The first line contains the length of side AB.
The second line contains the length of side BC.
Constraints
0 < AB <= 100
0 < BC <= 100
Lengths AB and BC are natural numbers.
Output Format
Output MBC in degrees.
Note: Round the angle to the nearest integer.
Examples:
If angle is 56.5000001°, then output 57.
If angle is 56.5000000°, then output 57°.
If angle is 56,4999999°, then output 56°.
0° <0° 90°
Sample Input
10
10
Sample Output
45°'''
import math
length_ab = int(input())
length_bc = int(input())

angle_mcb = math.atan(length_ab/length_bc)
angle_mcb_to_degree = round(math.degrees(angle_mcb))
print(angle_mcb_to_degree,chr(176),sep='')