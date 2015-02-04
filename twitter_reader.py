import sys
import requests
import json
from requests_oauthlib import OAuth1
from urlparse import parse_qs

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "FvHpVtiweeZ1Db4Q89AtXYmHE"
CONSUMER_SECRET = "vMZ0Ek28yv3jcnjVh4GDwMvAwPbyuT0VsA5qJNAYxDzP8iirnX"

# have to generate before using.  Remove before uploading to github
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""


def setup_oauth():
	"""Authorize your app via identifier."""
	# Request token
	oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
	r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
	credentials = parse_qs(r.content)

	resource_owner_key = credentials.get('oauth_token')[0]
	resource_owner_secret = credentials.get('oauth_token_secret')[0]

	# Authorize
	authorize_url = AUTHORIZE_URL + resource_owner_key
	print 'Please go here and authoirze: '+authorize_url

	verifier = raw_input('Please input the verifier: ')
	oauth = OAuth1(CONSUMER_KEY,
				   client_secret=CONSUMER_SECRET,
				   resource_owner_key=resource_owner_key,
				   resource_owner_secret=resource_owner_secret,
				   verifier=verifier)

	# finally, obtain the access token
	r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
	credentials = parse_qs(r.content)
	token = credentials.get('oauth_token')[0]
	secret = credentials.get('oauth_token_secret')[0]

	print "OAUTH_TOKEN: "+token
	print "OAUTH_TOKEN_SECRET: "+secret
	print

def get_oauth():
	oauth = OAuth1(CONSUMER_KEY,
				   client_secret=CONSUMER_SECRET,
				   resource_owner_key=OAUTH_TOKEN,
				   resource_owner_secret=OAUTH_TOKEN_SECRET)
	return oauth

def get_hashtags(json_obj):
	for tag in json_obj['entities']['hashtags']:
		print tag['text']

def get_gps_coords(json_obj):
	if json_obj['geo']:
		lat, lon = json_obj['geo']['coordinates']
		return (lat, lon)
	else:
		print 'geo tagging not enabled'
		return (None, None)

def home_timeline_request():
	oauth = get_oauth()
	r = requests.get(url="https://api.twitter.com/1.1/statuses/home_timeline.json?count=200", auth=oauth).json()

	return r

def search_request():
	oauth = get_oauth()
	request_url="https://api.twitter.com/1.1/search/tweets.json?q=place%3Afd70c22040963ac7&count=200"
	print request_url
	r = requests.get(url=request_url, auth=oauth).json()

	return r

def main():
	if not OAUTH_TOKEN:
		setup_oauth()
	else:
		json_obj = search_request()
		f = open('twitter_gps.csv', 'w')
		for obj in json_obj['statuses']:
			lat, lon = get_gps_coords(obj)
			string = '{0},{1}\n'.format(lat, lon)
			f.write(string)
		
		f.close()

if __name__ == "__main__":
	main()