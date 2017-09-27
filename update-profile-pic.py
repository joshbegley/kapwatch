import tweepy
import sys
import os

class KapwatchBot(object):

        def __init__(self, consumer_key, consumer_secret, access_token, token_secret):

                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, token_secret)
                self.twitter = tweepy.API(auth)

        def update_profile_image(self):
                self.twitter.update_profile_image('screenshot.png')

if __name__ == '__main__':
        from optparse import OptionParser
        parser = OptionParser()
        parser.add_option('--consumer_key', dest='consumer_key',
                        help="twitter consumer key")
        parser.add_option('--consumer_secret', dest='consumer_secret',
                        help="twitter consumer secret")
        parser.add_option('--access_token', dest='access_token',
                        help="twitter token key")
        parser.add_option('--token_secret', dest='token_secret',
                        help="twitter token secret")
        (options, args) = parser.parse_args()

        bot = KapwatchBot(options.consumer_key, options.consumer_secret,
                        options.access_token, options.token_secret)

        bot.update_profile_image()
