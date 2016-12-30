import os 
from markovbot import MarkovBot

# Initialise a MarkovBot instance
tweetbot = MarkovBot()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
book = os.path.join(dirname, 'Alex_Data.txt')
# Make your bot read the book!
tweetbot.read(book)

my_first_text = tweetbot.generate_text(5, seedword=['I', 'alive'])
print("tweetbot says:")
print(my_first_text)

# ALL YOUR SECRET STUFF!
# Consumer Key (API Key)
cons_key = 'RziMTIlFG2BDopROcYFyJNRxx'
# Consumer Secret (API Secret)
cons_secret = 'wFeEpLSQEJ3Ub628UIB3W04jRqjKiGIgCxTF1LXBLeFCkWQ9xD'
# Access Token
access_token = '814680840869322752-1oTZZzkHoBb3qfaFTxuraZ4ohRsFith'
# Access Token Secret
access_token_secret = '2bYfrjaDq9fFNzNSxZbF6MNVRWtNJ45e9bA14yXrziil5'

# Log in to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

# Set some parameters for your bot
targetstring = 'AlexBotLives'
keywords = ['hello', 'kill', 'food', 'star wars', 'etsy']
prefix = None
suffix = '#AlexBot'
maxconvdepth = 2

# Start auto-responding to tweets
tweetbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)

# Use the following to stop auto-responding
# (Don't do this directly after starting it, or your bot will do nothing!)
# tweetbot.twitter_autoreply_stop()

# Start periodically tweeting
tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=5, keywords=None, prefix=None, suffix='#AlexBot')

# Use the following to stop periodically tweeting
# (Don't do this directly after starting it, or your bot will do nothing!)
# tweetbot.twitter_tweeting_stop()

raw_input("\nPress enter to continue \n")
