'''
Reverse a String - Enter a string and the program will reverse it and print it out.
'''

in_string = input('Enter a string you wish to reverse: ')
print('The string you entered reversed is: '+ str(in_string[::-1]))

# Again using a while loop
in_string = input('Enter another string you wish to reverse: ')
output = ''
index = len(in_string)
while index:
	index-=1
	output+=in_string[index]
print('Using a while loop the string you entered reversed is: '+ str(output))

