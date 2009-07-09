#!/usr/bin/env python

from twyt import twitter, data         
import codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)  
import time
                                                      
total_to_fetch = 3200
count = 200

t = twitter.Twitter()
t.set_auth("username", "password")
                            
messages = []
remaining_messages_to_fetch = total_to_fetch - count
page = 1                   
while remaining_messages_to_fetch >= 0:                             
	fetched_timeline = t.status_mentions_timeline(count=count, page=page)
	status_list = data.StatusList(json=fetched_timeline)
	messages.extend(status_list)
	remaining_messages_to_fetch = remaining_messages_to_fetch - count
	page = page + 1

for m in messages:                                                        
	# Dirty hack to make the timestamp print in localtime
	stamp = time.strftime("%a %b %d %H:%M:%S %Y %Z", time.localtime(time.mktime(time.strptime("%s UTC" % m.created_at, "%a %b %d %H:%M:%S +0000 %Y %Z")) + 28800)) 
	print m.user.screen_name + " - " + stamp + " [ http://twitter.com/" + m.user.screen_name + "/status/" + str(m.id) + " ]" + " (" + m.source + ")"
	print m.text
	print "--------------------"