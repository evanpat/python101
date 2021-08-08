import json
import requests
import time

api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjczMzE2NWMzLTljNjAtNGEzZi04OTZiLTU4NjJiZGFlODBjYSIsImlhdCI6MTYyODQxMDY0NCwic3ViIjoiZGV2ZWxvcGVyLzA1NGE3NTI4LTZlNGQtYzA0NS0zYzg2LTBmMjg3MzkxYjEzNCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMC4wLjAuMCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.IAStyGNXCdxXymYV2UkxwML3sBrkte-DrNu6_4sabW2qCPMFDE-nTffsE-Nso7tXFqLfgYmwhlc20qnW8ioTZA"
api_key2 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM4ODVhNzg1LWE3NmUtNDY0OS1hM2NlLTM0NDNlYjAyZWVhNSIsImlhdCI6MTYyODQxMzA5Nywic3ViIjoiZGV2ZWxvcGVyLzA1NGE3NTI4LTZlNGQtYzA0NS0zYzg2LTBmMjg3MzkxYjEzNCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMjEwLjYuMTkyLjE4Il0sInR5cGUiOiJjbGllbnQifV19.6Z6csfJFNwxqI3cHddrlBv14UlA7js0ALvYMqVjZOyeBg8KuP1v5vV5QS1naOV0QJbtt0Vvgv373zeoLNoS6gg"
ts = time.time()
r = requests.get(
    "https://api.brawlstars.com/v1/players/%23GVY8J8RC/",
    #headers = {"Accept": "application/json"},
    headers = {"authorization": "Bearer " + api_key2}
)

#curl -X GET --header 'Accept: application/json' --header "authorization: Bearer <API token>" 'https://api.brawlstars.com/v1/players/GVY8J8RC/battlelog'
print(r.content)

c = r.content
cc = json.loads(c)
print(json.dumps(cc, indent=2))

#print(f'my login is {cc["login"]}')

if r:
    print('Success!', r.status_code)
else:
    print('An error has occurred.', r.status_code)