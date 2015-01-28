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

OAUTH_TOKEN = "156509990-2OENzM4s6crQlUI9V6geS54tGEN0pEQVQ7Pvb2Xr"
OAUTH_TOKEN_SECRET = "szk6SWcmyRSSW5ECQRKyFyFkERj62cU1WRdydPSdMP8EU"


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

	return token, secret

def get_oauth():
	oauth = OAuth1(CONSUMER_KEY,
				   client_secret=CONSUMER_SECRET,
				   resource_owner_key=OAUTH_TOKEN,
				   resource_owner_secret=OAUTH_TOKEN_SECRET)
	return oauth

if __name__ == "__main__":
	if not OAUTH_TOKEN:
		token, secret = setup_oauth()
		print "OAUTH_TOKEN: "+token
		print "OAUTH_TOKEN_SECRET: "+secret
		print
	else:
		oauth = get_oauth()
		r = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?count=1", auth=oauth)
		result=str(r.json())
		result = json.dumps(result,indent=1)
		f = open('results.json', 'w')
		f.write(result)
		f.close()
		sys.exit(0)