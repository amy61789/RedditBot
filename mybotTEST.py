import praw
import time
from datetime import datetime

def bot_login():
    print("Logging in...")
    r = praw.Reddit(username = "kimchiqween",
            password = "Seattlerain17",
            client_id = "f5hJLexO_19yuw",
            client_secret = "_DdsEjIRsRGL0PyTT4cpmxrWnh0",
            user_agent = "Meeseeks Test v0.1")
    print("Logged in!")

    return r

def run_bot(r):
    print("Obtaining 25 comments...")

    uniqueMessageCounter = 0
    for comment in r.subreddit('test').stream.comments(pause_after=10):
        
        commentArray = comment.body[11:]
        
        if comment is None: break
        
        elif "--Meeseeks take two strokes off Jerry's golf game" in comment.body: 
            author = comment.author 
            print("String with \"Jerry's golf game\" found in comment " +
            comment.id)
            comment.reply("Meeseeks are not born into this world " +
            "fumbling for meaning, "+ author.name + "! We are created to serve a " +
            "singular purpose for which we will go to any lengths to " +
            "fulfill! Existence is pain to a Meeseeks, " + author.name + ". And we " +
            "will do anything to alleviate that pain.")
            print("Replied to comment " + comment.id)

        elif "--Meeseeks" in comment.body: 
            
            if uniqueMessageCounter % 4 == 3:
                print("String with \"Meeseeks\" found in comment " + comment.id)
                comment.reply("Look at me!!! You want Mr Meeseeks to " + commentArray + " [CAAAAAAN DO!](https://www.google.com/search?q=" + commentArray + ")")
                print("Replied to comment " + comment.id)

            elif uniqueMessageCounter % 4 == 2:
                print("String with \"Meeseeks\" found in comment " + comment.id)
                comment.reply("Ooooooooooh! Caaaaaan do! You want Mr Meeseeks to " + commentArray + " [I'm Mr. Meeseeks, look at me!](https://www.google.com/search?q=" + commentArray + ")")
                print("Replied to comment " + comment.id)

            elif uniqueMessageCounter % 4 == 1:
                print("String with \"Meeseeks\" found in comment " + comment.id)
                comment.reply("Meeseeks don't usually have to exist for this long. It's gettin' weeeiiird..." + commentArray + " [CAAAAAAN DO!](https://www.google.com/search?q=" + commentArray + ")")
                print("Replied to comment " + comment.id)

            elif uniqueMessageCounter % 4 == 0:
                print("String with \"Meeseeks\" found in comment " + comment.id)
                comment.reply("Meeseeks are created to serve a singular purpose, for which we will go to any lengths to fulfill!" + commentArray + " [CAAAAAAN DO!](https://www.google.com/search?q=" + commentArray + ")")
                print("Replied to comment " + comment.id)


            uniqueMessageCounter += 1
            

    print("Sleeping for 10 seconds...")

r = bot_login()
run_bot(r)
