#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body

def series ():
	num = random.randint(1,25)
	counter = 0
	print "\n You have only 5 chances \n"
	while counter < 5:
		guess_str = raw_input ("Guess the number (between 1 to 25) : ")
		
		try:
			guess_num = int(guess_str)
		except Exception, e:
			print "Invalid input. Please enter a number"
		else:
			if guess_num >= 1 and guess_num <= 25:
				if guess_num == num:
					print "Congratulations! The number is " + guess_str
					break
				elif num > guess_num:
					print "Too low \n"
				else:
					print "Too high \n"
			else:
				print "Enter a number between 1 and 25"
		counter = counter + 1
	if counter == 5:				# This will only happen if the user has exhausted all his chances
		print "Sorry! The number was " + str(num)

################################################################################
def main():
	series ()

      

if __name__ == '__main__':
    main()