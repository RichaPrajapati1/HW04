#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body
def counter (word, letter):
	count = 0
	for char in word:
		if char == letter:
			count = count + 1
	print "Count of " +letter + " in " + word + " is : " + str(count)

################################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    counter ('banana','a')
    counter ('richa','e')
    

if __name__ == '__main__':
    main()