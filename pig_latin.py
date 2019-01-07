'''
Pig Latin - Pig Latin is a game of alterations played on the English language game. 
To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed 
(Ex.: "sloppy" would yield loppy-say). 
'''

def pig_latin(word):
	vowels = ['a','e','i','o','u']
	if word[0] not in vowels:
		word = word[1:] + '-' + word[0] + 'ay'
	return word

in_string = input('Please enter the word you wish to convert to Pig Latin: ')
print('The Pig Latin version of '+ str(in_string)+' is '+str(pig_latin(in_string)))
