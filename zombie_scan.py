#!/usr/bin/python2.7
import string
import codecs
import json
from nsapi import api_request
from sys import argv

region = argv[1]

author = 'Eluvatar'
user = argv[2]

user_agent = "Zombie Scanner by %s being run by %s"%(author, user)

res = []

nations = api_request({'region':region,'q':'nations'},user_agent).find('NATIONS').text.split(':')

for nat in nations:
        try:
            entry = {"name":nat}
            natxml = api_request({'nation':nat,'q':'zombie'},user_agent)
            zx = natxml.find('ZOMBIE')
            entry["action"] = zx.find('ZACTION').text
            entry["zombies"] = int(zx.find('ZOMBIES').text)
            entry["survivors"] = int(zx.find('SURVIVORS').text)
            entry["dead"] = int(zx.find('DEAD').text)
            res.append(entry)
        except:
            pass
out    = open('zombie_info.json','w')
json.dump(res, out, separators=(',',':'))
