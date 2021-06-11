#magic 8 ball
import random
messages = ["It is certain", 
"It is decidedly so",
"yes definetly",
"reply hazy try again",
"ask again later",
"concentrate and ask again",
"my reply is no",
"outlook not so good",
"very doubtful"]
print(messages[random.randint(0, len(messages) -1)])
