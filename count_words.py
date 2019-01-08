'''
Count Words in a String - Counts the number of individual words in a string. 
For added complexity read these strings in from a text file and generate a summary.
'''

# Simple - string count

# def word_count(text):
# 	text = text.split()
# 	count = 0
# 	for word in text:
# 		count+=1
# 	return count

# in_string = input("Please enter some text to count the number of words: ")
# print(word_count(in_string))


# Complex - Read from text file

def word_count(text):
	text = text.split()
	count = 0
	for word in text:
		count+=1
	return count

p = open('string.txt','r')
try:
    text = p.read()
    print(word_count(text))
except:
    print('An exception was raised!')
finally:
    p.close()





