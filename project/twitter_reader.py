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

def main():
	url="https://api.twitter.com/1.1/search/tweets.json?q=place%3Afd70c22040963ac7&count=200"
	json_obj = apiRequest.search_request(url)
	#json_obj = apiRequest.home_timeline_request()
	f = open('twitter_gps.csv', 'a')
	for obj in json_obj['statuses']:
		lat, lon = get_gps_coords(obj)
		string = '{0},{1}\n'.format(lat, lon)
		f.write(string)

	f.close()

if __name__ == "__main__":
	main()
