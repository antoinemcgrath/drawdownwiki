#!/usr/bin/env python3

import mwclient
import re
import os
import json
import time
import csv

#### Load API keys file
#### First add login keys to local keychain ( To /usr/local/keys.json added   "DrawDownWiki":{"User": A_Admin,  "Access": "USEROPASSWORD}, )
keys_json = json.load(open('/usr/local/keys.json'))

#### Specify key dictionary wanted (generally [Platform][User][API])

Keys = keys_json["DrawDownWiki"]

#### Access your MW with bot/admin approved permissions
login_user = Keys['User']
login_password = Keys['Access']

#### Set path to mediawiki
site = mwclient.Site(('http', 'www.DrawDownWiki.info'), path='/',)
site.login(login_user, login_password)

#### Set edit notes and counter
ua = 'Gen_Script run by A_Admin Bot' #UserAgent bot note
save_note = "Find&Replace Script added _talk_3 to existing Solution Aricles"
default = "" #Create a result for dictionary response when key does not occure
count = 0

SpecifiedCategory="SolutionArticle"

#################################################

old_A = ("|_talk_1=\n\
|_talk_2=\n\
}}")

new_A = ("|_talk_1=\n\
|_talk_2=\n\
|_talk_3=\n\
}}")

for a_page in site.Categories[SpecifiedCategory]:
    articlepage = site.Pages[a_page]
#for a_page in site.search('" (USA CA)"'):
#    print (a_page)
    #articlepage = a_page['title']
    #articlepage = site.Pages[articlepage]
    profiletext = articlepage.text()
    print(profiletext)
    print("Updated: " + str(articlepage.name.encode('utf-8')))
    newtext = (profiletext).replace(old_A,new_A)
    #print(newtext.encode('utf-8'))
    articlepage.save(newtext, save_note)
    time.sleep(5)
    print("UPDATED!")
