'''
RSS Feed Creator - Given a link to RSS/Atom Feed, get all posts and display them.
Dependency = feedparser
Reuters RSS = http://feeds.reuters.com/Reuters/worldNews
'''

import feedparser

in_string = input('Please enter the URL of an RSS feed or press ENTER to see default (BBC): ')

if in_string == '':	
	rss = "http://feeds.bbci.co.uk/news/world/rss.xml" 
else:
	rss = in_string

feed = feedparser.parse(rss)

for news in feed["items"]:
	print(news["updated"], '\t', news["title"])
