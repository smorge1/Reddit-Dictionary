import praw

from PyDictionary import PyDictionary

#import requests
#from bs4 import BeautifulSoup
#import html5lib
import re

dictionary = PyDictionary()

#def scrape(word):
#    url = "https://www.merriam-webster.com/dictionary/"
#    url = url + word
#    html = requests.get(url)
#    soup = BeautifulSoup(html.text, 'html5lib')
#    text = soup.prettify()
#    print text
#    
#    BeautifulSoup()

def validWord(word):
    if word.isalpha():
        return word
    
    regex = re.compile('[^a-zA-Z\']')
    newWord = regex.sub('', word)
    return newWord

def define(word):
    definition = dictionary.meaning(word)
    

    if definition == None or len(definition) == 0:
        print("Cannot find word")
        return


    print "**" + word.title() + "**"
    print
        
    for item in definition:
        print "*" + item + "*"
        print
        for sentence in definition[item]:
            print "* " + str(sentence.capitalize()) + "."
            print

    syn = dictionary.synonym(word)
    print "*Synonyms*:"
    print
    for item in syn:
        print "*", item.title()
        print

    ant = dictionary.antonym(word)
    print "*Antonyms*:"
    print
    for item in ant:
        print "*", item.title()
        print
    
def bot():
    reddit = praw.Reddit('bot1')

    subreddit = reddit.subreddit("test")

    for submission in subreddit.new(limit=1):
    
        comments = submission.comments
        if(len(comments) != 0):
            for comment in comments:
                commentBody = comment.body
                print(commentBody)
                words = commentBody.split(" ")
            
                if(len(words) != 0):
                    for word in words:
                        print(word)
                        #if words[wordNum].lower() == "!Define".lower():
                        #    print("test")
        
        
def main():
    word = raw_input("Word to define? ")
    word = validWord(word)
    define(word)    
    
main()