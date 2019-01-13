# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 08:17:10 2019

@author: Byen23
"""

# This will be the 10th Program to be uploaded to github

"""Conditional Iteration: The while Loop"""

""" The following example is a short script that prompts the user for a series of numbers, computes their sum, and outputs the result. Instead of forcing the user to enter a definite number of values, the program stops the input process when the user simply presses the return or enter key. The program recognizes this value as the empty string. We first present a rough draft in the form of a pseudocode algorithm:"""

# 1.Set the sum to 0.0
# 2.Input a string
# 3.While the string is not the empty string
#	 4.Convert the string to a float
#	 5.Add the float to the sum
#	 6.Input a string
# 7.Print the sum

theSum = 0.0 #1

data = input("Enter a number or just enter to quit: ") #2
while data != "": 	#3
	number = float(data)	#4
	theSum += number 	#5
	data = input("Enter a number or just enter to quit: ")	#6
print("The sum is", theSum)	#7



