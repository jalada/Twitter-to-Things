#!/usr/bin/python
import twitter
import os, sys

# The Twitter username & password of your gateway account
t_user = 'username'
t_pass = 'password'

osacommand = 'osascript ' + sys.path[0] + '/twitter-things.scpt '

api = twitter.Api(username=t_user, password=t_pass)

filename = sys.path[0] + '/since'

try:
	if not os.path.exists(filename):
		f = open(filename, 'w')
		f.write('0')
		f.close()
	f = open(filename, 'r+')
except IOError:
	raise Exception("Something bad happened creating/reading the since file")

try:
	since = int(f.read())
except ValueError:
	raise Exception("Something is wrong with your 'since' file.")

if since:
	dms = api.GetDirectMessages(since_id=since)
else:
	dms = api.GetDirectMessages()

for dm in dms:
	if (dm.id > since) or not since:
		since = dm.id
	os.system(osacommand + '"' + dm.text.replace("\"", "\\\"") + '"')

f.seek(0)
f.write(str(since))
f.close()