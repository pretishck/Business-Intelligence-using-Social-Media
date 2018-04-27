import json
tweets = []

for line in open('tweets3.json'):
  try: 
    tweets.append(json.loads(line))
  except:
    pass

ids = [T['id_str'] for T in tweets if 'id_str' in T]
texts = [T['text'] for T in tweets if 'text' in T]
times = [T['created_at'] for T in tweets if 'created_at' in T]
screen_names = [T['user']['screen_name'] for T in tweets if 'user' in T]
names = [T['user']['name'] for T in tweets if 'user' in T]
mentions1 = [(T['entities']['user_mentions'][0]['screen_name'] if len(T['entities']['user_mentions']) >= 1 else None) for T in tweets if 'entities' in T ]
mentions2 = [(T['entities']['user_mentions'][1]['screen_name'] if len(T['entities']['user_mentions']) >= 2 else None) for T in tweets if 'entities' in T]
hashtags1 = [(T['entities']['hashtags'][0]['text'] if len(T['entities']['hashtags']) >= 1 else None) for T in tweets if 'entities' in T]
hashtags2 = [(T['entities']['hashtags'][1]['text'] if len(T['entities']['hashtags']) >= 2 else None) for T in tweets if 'entities' in T]
urls1 = [(T['entities']['urls'][0]['expanded_url'] if len(T['entities']['urls']) >= 1 else None) for T in tweets if 'entities' in T]
urls2 = [(T['entities']['urls'][1]['expanded_url'] if len(T['entities']['urls']) >= 2 else None) for T in tweets if 'entities' in T]
lats = [(T['geo']['coordinates'][0] if T['geo'] else None) for T in tweets if 'geo' in T]
lons = [(T['geo']['coordinates'][1] if T['geo'] else None) for T in tweets if 'geo' in T]
place_names = [(T['place']['full_name'] if T['place'] else None) for T in tweets if 'place' in T]
place_types = [(T['place']['place_type'] if T['place'] else None) for T in tweets if 'place' in T]

out = open('tweets3.csv', 'w')
print >> out, 'id,created,text,screen name,name,mention 1,mention 2,hashtag 1,hashtag 2,url 1,url 2,lat,lon,place name,place type'

rows = zip(ids, times, texts, screen_names, names, mentions1, mentions2, hashtags1, hashtags2, urls1, urls2, lats, lons, place_names, place_types)

from csv import writer
csv = writer(out)

for row in rows:
    values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
    csv.writerow(values)

out.close()


