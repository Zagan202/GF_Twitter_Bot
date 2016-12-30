import os 
from markovbot import MarkovBot

# Initialise a MarkovBot instance
tweetbot = MarkovBot()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
book = os.path.join(dirname, 'Freud_Dream_Psychology.txt')
# Make your bot read the book!
tweetbot.read(book)

my_first_text = tweetbot.generate_text(5, seedword=['I', 'sass'])
print("tweetbot says:")
print(my_first_text)

# ALL YOUR SECRET STUFF!
# Consumer Key (API Key)
cons_key = 'WnnlPi8m01yhrR6xM5jgDPY2u'
# Consumer Secret (API Secret)
cons_secret = '0g7ChS7wKBAEpyoj4Q9jVRuAgi7kCY7ux0FLSHS8oRriPYKl7R'
# Access Token
access_token = '1852893697-YKvNV0LZGMgPf05kOkz4NbY80ZGmxZxRx7QHwjf'
# Access Token Secret
access_token_secret = '4ClpZRSFmRLHwRoccfn4mhBcxxImTM1fyryFMDLszHAu3'

# Log in to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

# Set some parameters for your bot
targetstring = 'MarryMeFreud'
keywords = ['marriage', 'ring', 'flowers', 'children', 'religion']
prefix = None
suffix = '#FreudSaysIDo'
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