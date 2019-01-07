'''
Count Vowels - Enter a string and the program counts the number of vowels in the text. 
For added complexity have it report a sum of each vowel found.
'''

# Simple approach - no sum of each vowel
# def count_vowels(text):
# 	vowels = ['a','e','i','o','u']
# 	count = 0
# 	for let in text:
# 		if let in vowels:
# 			count+=1
# 	return count

# With added complexity
def count_vowels(text):

	text = text.lower()
	count_a = count_e = count_i = count_o = count_u = 0

	for let in text:
		if let == 'a':
			count_a +=1
		if let == 'e':
			count_e +=1
		if let == 'i':
			count_i +=1
		if let == 'o':
			count_o +=1
		if let == 'u':
			count_u +=1

	return parse_result(count_a, count_e, count_i, count_o, count_u)


def parse_result(count_a, count_e, count_i, count_o, count_u):
	
	if count_a != 0:
		print(str(count_a)+" a's")
	if count_e != 0:	
		print(str(count_e)+" e's")
	if count_i != 0:
		print(str(count_i)+" i's")
	if count_o != 0:
		print(str(count_o)+" o's")
	if count_u != 0:
		print(str(count_u)+" u's")

in_string = input("Please enter some text to count the number of vowels: ")
print(str(in_string)+', has: ')
count_vowels(in_string)
