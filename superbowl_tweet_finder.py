import datetime
import json
import requests

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKzrlgEAAAAAht6dzPN67U8IuexfSMWN279WB4c%3DyYf2sq8wgmczA0jFyhL14x5zk2QEvDpkietkahQDoiHQuAks7V'

params = {'query': '#superbowl',
          'start_time': '2023-02-09T19:14:00.52Z', # Convert to MST (UTC - 7), Superbowl starts 4:30 PM MST
          'tweet.fields': 'text,created_at,referenced_tweets',
          'max_results': '10'}
headers = {'Authorization': 'Bearer ' + BEARER_TOKEN}
r = requests.get('https://api.twitter.com/2/tweets/search/recent', params=params, headers=headers)

tweets = r.json()
with open("superbowl_tweets.txt", "w") as file:
    for tweet in tweets['data']:
        # print(tweet['referenced_tweets'][0]['type'])
        file.write(tweet['created_at'] + ',' + tweet['text'].replace('\n', ' ') + "\n")