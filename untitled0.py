# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:17:01 2013

@author: smallz
"""

import urllib
import datetime

SD = [] #all year and month list
SPlist = [] #price

for x in range(1993,int(datetime.datetime.now().strftime('%Y'))+1): #create all year and month
    if x != int(datetime.datetime.now().strftime('%Y')):
        for y in range(1,13):
            if y < 10:
                spdate = str(x) + '0' + str(y)                
            else:
                spdate = str(x) + str(y)
            '''print spdate''' #verify date
            SD.append(spdate)
    else:
        for y in range(1,int(datetime.datetime.now().strftime('%m'))+1):
            if y < 10:
                spdate = str(x) + '0' + str(y)
            else:
                spdate = str(x) + str(y)
            '''print spdate''' #verify date
            SD.append(spdate)
            
spnumber = '2314'
            
for sddate in SD: 
    url = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAY_print.php?genpage=genpage/Report' \
    + sddate + '/' + sddate +'_F3_1_8_' + spnumber + '.php&type=csv'  
    response = urllib.urlopen(url)  
    html = response.read()  
    sp = html.splitlines()
    del sp[0:2]
    if sp != []:
        SPlist.extend(sp)
print SPlist