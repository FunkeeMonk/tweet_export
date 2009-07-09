#!/usr/bin/env python

from twyt import twitter, data         
import codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)  
import time

#additional_status = (389314822,
#389943372,
#389960372,
#392022802,
#394018232)
#
count = 200

t = twitter.Twitter()
t.set_auth("username", "password")
                            
messages = []
messages_to_fetch = 3200 - count
page = 1                   
while messages_to_fetch >= 0:                             
	fetched_timeline = t.status_user_timeline(count=count, page=page)
	status_list = data.StatusList(json=fetched_timeline)
	messages.extend(status_list)
	messages_to_fetch = messages_to_fetch - count
	page = page + 1

#for status in additional_status:
#	fetched_status = t.status_show(str(status))
#	d = data.Status()
#	d.load_json(fetched_status)
#	messages.append(d)
#
for m in messages:                                                        
	# Dirty hack to make the timestamp print in localtime
	stamp = time.strftime("%a %b %d %H:%M:%S %Y %Z", time.localtime(time.mktime(time.strptime("%s UTC" % m.created_at, "%a %b %d %H:%M:%S +0000 %Y %Z")) + 28800)) 
	print stamp + " [" + str(m.id) + "]" + " (" + m.source + ")"
	print m.text
	print "--------------------"