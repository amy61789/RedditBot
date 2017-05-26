import praw
import time
from datetime import datetime

def bot_login():


    return r

def run_bot(r):
    print("Obtaining 25 comments...")
    currentTime = datetime.utcnow()
    uniqueMessageCounter = 0
    for comment in r.subreddit('test').stream.comments(pause_after=10):
        
        if comment is None: break
        
        elif "--Meeseeks take two strokes off Jerry's golf game" in comment.body and time.mktime(currentTime.timetuple()): #< comment.created_utc:
            author = comment.author 
            print("String with \"Jerry's golf game\" found in comment " +
            comment.id)
            commentArray = comment.body.split("\n")
            comment.reply("Meeseeks are not born into this world " +
            "fumbling for meaning, "+ author.name + "! We are created to serve a " +
            "singular purpose for which we will go to any lengths to " +
            "fulfill! Existence is pain to a Meeseeks, " + author.name + ". And we " +
            "will do anything to alleviate that pain.")
            print("Replied to comment " + comment.id)
            #print(comment.created_utc)

        elif "--Meeseeks" in comment.body and time.mktime(currentTime.timetuple()): #< comment.created_utc:
            
            if uniqueMessageCounter % 4 == 3:
                print("String with \"Meeseeks\" found in comment " + comment.id)
                commentArray = comment.body.split("\n")
                comment.reply("UNIQUE1Look at me!!! You want Mr Meeseeks to " + commentArray[1] + " [CAAAAAAN DO!](https://www.google.com/search?q=" + commentArray[1] + ")")
                print("Replied to comment " + comment.id)
                #print(comment.created_utc)
            elif uniqueMessageCounter % 4 == 2:
                print("String with \"Meeseeks\" found in comment " + comment.id)
                commentArray = comment.body.split("\n")
                comment.reply("UNIQUE2Look at me!!! You want Mr Meeseeks to " + commentArray[1] + " [CAAAAAAN DO!](https://www.google.com/search?q=" + commentArray[1] + ")")
                print("Replied to comment " + comment.id)
                #print(comment.created_utc)
            elif uniqueMessageCounter % 4 == 1:
                print("String with \"Meeseeks\" found in comment " + comment.id)
                commentArray = comment.body.split("\n")
                comment.reply("UNIQUE3Look at me!!! You want Mr Meeseeks to " + commentArray[1] + " [CAAAAAAN DO!](https://www.google.com/search?q=" + commentArray[1] + ")")
                print("Replied to comment " + comment.id)
                #print(comment.created_utc)
            elif uniqueMessageCounter % 4 == 0:
                print("String with \"Meeseeks\" found in comment " + comment.id)
                commentArray = comment.body.split("\n")
                comment.reply("UNIQUE4Look at me!!! You want Mr Meeseeks to " + commentArray[1] + " [CAAAAAAN DO!](https://www.google.com/search?q=" + commentArray[1] + ")")
                print("Replied to comment " + comment.id)
                #print(comment.created_utc)

            uniqueMessageCounter += 1
            

    print("Sleeping for 10 seconds...")

r = bot_login()
run_bot(r)
