#!/usr/bin/env python
# HW04_ex07_04

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:
    
#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes the
# resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

################################################################################
# Imports

#######This is incomplete..Dont evaluate

# Body
def eval_loop():
	s = ''
	while True:
		input_str = raw_input ("Enter an expression: ")
		if input_str == 'done':
			break
		try:
			eval(input_str)
		except Exception, e:
			print "Enter a valid expression"
		else:
			print eval(input_str)



################################################################################
def main():
    eval_loop()
    

if __name__ == '__main__':
    main()