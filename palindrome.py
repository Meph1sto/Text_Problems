'''
Check if Palindrome - Checks if the string entered by the user is a palindrome. 
That is that it reads the same forwards as backwards like “racecar”
'''

in_string = input('Please enter the word you wish to check is a palindrome: ')
if in_string == in_string[::-1]:
	print(in_string + ' is a palindrome')
else:
	print(in_string + ' is not a palindrome')