#!/usr/bin/python2.7
#   Simple script to observe the zombie status of nations in a region 
#   Copyright (C) 2013-2014 Eluvatar
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import string
import codecs
import json
from nsapi import api_request
from sys import argv

if( len(argv) < 3 ):
    print "usage: ./zombie_scan <region> <user>"
    print "(user must be a valid identifier of you as required by http://www.nationstates.net/pages/api.html#terms )"
    exit()

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
