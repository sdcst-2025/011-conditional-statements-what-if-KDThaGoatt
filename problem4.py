#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""

import math

a = float(input("Enter the first side"))
b = float(input("Enter the second side"))
c = float(input("Enter the third side"))

v1 = min(a,b,c)
v3 = max(a,b,c)
v2 = (a + b + c) - (v1+v3)

expected = math.sqrt(v1**2 + v2**2)
lowLimit = (expected * 0.98)
upLimit = (expected / 0.98)

if (lowLimit < v3 < upLimit):
    print("that is a right triangle")

elif (v1**2 + v2**2 < v3**2):
    print("that is an obtuse triangle")

else:
    print("that is an acute triangle")

# actual short side
# actual long side
# actual hypotenuse

# find expected hypotenuse
# find lower limit for expected hypotenuse
# find upper limit

#if lower < actual < upper
#right