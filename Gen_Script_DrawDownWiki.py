#!/usr/bin/env python3

import mwclient
import re
import os
import json
import csv
import time

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
save_note = "A_Admin Bot Gen_Script_DrawDownWiki.py creating articles"
default = "" #Create a result for dictionary response when key does not occure
count = 0

#### Import CSV
with open('/Users/macbook/GIT/DrawDownWiki/documentation/AllDrawDownArticles.csv', 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=';')
    csv_list = list(data)

#### 1st row are labels, 2nd row variable_names)
row_label = csv_list.pop(0) #Assign & cut out first item in list
row_variable_name = csv_list.pop(0) #Assign & cut out first item in list
Total_Articles_Count = len(csv_list)

category = "[[Category:SolutionArticle]]"

#################################################

for Article in csv_list:
    count += 1
    '''
    print(row_label[0], row_variable_name[0], Article[0])
    print(row_label[1], row_variable_name[1], Article[1])
    print(row_label[2], row_variable_name[2], Article[2])
    print(row_label[3], row_variable_name[3], Article[3])
    print(row_label[4], row_variable_name[4], Article[4])
    print(row_label[5], row_variable_name[5], Article[5])
    print(row_label[6], row_variable_name[6], Article[6])
    print(row_label[7], row_variable_name[7], Article[7])
    print(row_label[8], row_variable_name[8], Article[8])
    print(row_label[9], row_variable_name[9], Article[9])
    print(count, "of", Total_Articles_Count)
    print()
    '''
    #####################################################
    ## The Article Page Names were created with the following
    ## Then added to the .csv file in the final row
    #####################################################
    ## mw_article_name = Article[2].replace(" ", "_")
    ## mw_article_name = re.sub(r'[^a-zA-Z0-9\_\(\)]', ' ', mw_article_name)
    ## mw_article_name = mw_article_name.replace(" ", "_")
    ## mw_article_name = mw_article_name.replace("__", "_")
    ## mw_article_name = mw_article_name.replace("_", " ")
    #####################################################    print(row_label[3], row_variable_name[3], Article[3])

    body = (
          '|' + row_variable_name[0] + '=' + Article[0] +'\n'
        + '|' + row_variable_name[1] + '=' + Article[1] +'\n'
        + '|' + row_variable_name[2] + '=' + Article[2] +'\n'
        + '|' + row_variable_name[3] + '=' + Article[3] +'\n'
        + '|' + row_variable_name[4] + '=' + Article[4] +'\n'
        + '|' + row_variable_name[5] + '=' + Article[5] +'\n'
        + '|' + row_variable_name[6] + '=' + Article[6] +'\n'
        + '|' + row_variable_name[7] + '=' + Article[7] +'\n'
        + '|' + row_variable_name[8] + '=' + Article[8] +'\n'
        + '|' + row_variable_name[9] + '=' + Article[9] +'\n'
            )
    insert = '{{SolutionArticle' + '\n' + body + '|_talk_1=' + '\n' + '|_talk_2=' + '\n' + '|_talk_3=' + '\n' + '}}' + '\n' + '\n' + category
    insert = str(insert)

    a_page = site.Pages[Article[9]]
    if a_page.exists == False:
        a_page.save(insert, save_note)
        count = count + 1
        print (count)
    else:
        #print("Page already exists, will not overwrite")
        a_page.save(insert, save_note)
        count = count + 1
        print (count)
    time.sleep(10)
