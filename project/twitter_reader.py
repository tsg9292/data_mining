import apiRequest

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

def print_gps_coords(json_obj):
	f = open('twitter_gps.csv', 'a')
	for obj in json_obj['statuses']:
		lat, lon = get_gps_coords(obj)
		string = '{0},{1}\n'.format(lat, lon)
		f.write(string)

	f.close()

def main():
	#&place%3A96683cc9126741d1
	url="https://api.twitter.com/1.1/search/tweets.json?q=%23isis&count=200"
	#url="https://api.twitter.com/1.1/search/tweets.json?q=place%3Afd70c22040963ac7&count=200"
	#url="https://api.twitter.com/1.1/geo/search.json?query=United States"
	json_obj = apiRequest.search_request(url)
	#json_obj = apiRequest.home_timeline_request()

	f = open('results.txt','w')
	for tweet in json_obj['statuses']:

		#if 'retweeted_status' in tweet:
		#	print "Retweeted post; heres the original tweet: "
		#	print tweet['retweeted_status']['text']
		#	string = tweet['retweeted_status']['text'].encode('utf-8')+'\n'
		#	f.write(string)
		#else:
		#	print "Official tweet:"
		#	print tweet['text']
			#TODO make this work with encodings other than ascii eg: when there is arab text in a tweet.
		tweet['text'] = tweet['text'].replace('\n','')

		string = tweet['text'].encode('utf-8')+'\n'
		print string
		f.write(string)

	f.close()

if __name__ == "__main__":
	main()
