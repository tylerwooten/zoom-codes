from twython import Twython
from secret import Secret

zoomCodes = ['727 2954 5506']

TWITTER_APP_KEY = Secret.TWITTER_APP_KEY
TWITTER_APP_KEY_SECRET = Secret.TWITTER_APP_KEY_SECRET
TWITTER_ACCESS_TOKEN = Secret.TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET = Secret.TWITTER_ACCESS_TOKEN_SECRET

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

print('Starting Search...\n')

hashtags = ['#zoomclass', '#zoomcodes', '#zoombomb', '#zoomcode', '#zoombombing', '#ZOOMCODE', '#ZOOMCODES', '#ZOOMBOMB']
for tag in hashtags:
    search_results = t.search(q=tag, rpp="1000")

    for tweet in search_results["statuses"]:
        #print(tweet['text'], '\n')

        for code in zoomCodes:
            if code in tweet['text']:
                print(tweet)
                print("Tweet from @%s Date: %s" % (tweet['user']['screen_name'].encode('utf-8'),tweet['created_at']))
                print(tweet['text'], "\n")

print('Finished Search.\n')
