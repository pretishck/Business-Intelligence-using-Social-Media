from slistener import SListener
import time, tweepy, sys

## Eventually you'll need to use OAuth. Here's the code for it here.
## You can learn more about OAuth here: https://dev.twitter.com/docs/auth/oauth
consumer_key        = "mgPHYeCbUlxtiQqHMBqkWmwT4"
consumer_secret     = "1M9lMw5vgwB7OYNa22BTL8baM8Ud2kqf5LeuWJdOkb979S6bbb"
access_token        = "131507394-Y8QKluqHvmohEOIfTvjTwvBRd2As4QnxSCB1yFWZ"
access_token_secret = "UN41zQjZVTlUk1d4DBA99nyBE2Nw1qdpKznK6pxNziJ0Q"

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api= tweepy.API(auth)
def main( mode = 1 ):
    track  = ['oil']
    follow = []
            
    listen = SListener(api, 'test')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started on %s users and %s keywords..." % (len(track), len(follow))

    try: 
        stream.filter(track = track, follow = follow)
        #stream.sample()
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()