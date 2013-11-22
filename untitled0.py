# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:17:01 2013

@author: smallz
"""

import urllib
import datetime
import matplotlib.pyplot as plt

class SDate:
    
    def __init__(self): #initial SDate
        self.SD = []
        self.nowyear = int(datetime.datetime.now().strftime('%Y'))
        self.nowmonth = int(datetime.datetime.now().strftime('%m'))
        
    def ymdatelist(self): #get year & month value

        for x in range(1993,self.nowyear+1): #create all year and month
            if x != self.nowyear:
                for y in range(1,13):
                    if y < 10:
                        spdate = str(x) + '0' + str(y)                
                    else:
                        spdate = str(x) + str(y)
                        '''print spdate''' #verify date
                    self.SD.append(spdate)
            else:
                for y in range(1,self.nowmonth+1):
                    if y < 10:
                        spdate = str(x) + '0' + str(y)
                    else:
                        spdate = str(x) + str(y)
                        '''print spdate''' #verify date
                    self.SD.append(spdate)
                    
snumber = '2314'
SPdatalist = []
templist = []
spdate = []
sph = []
SDatelist = SDate()
SDatelist.ymdatelist()
         
for sddate in SDatelist.SD: #store url data into temp list
    url = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAY_print.php?genpage=genpage/Report' \
    + sddate + '/' + sddate +'_F3_1_8_' + snumber + '.php&type=csv'  
    response = urllib.urlopen(url)  #open url
    html = response.read()  #read url data
    sp = html.splitlines()  #split data into list
    response.close()        #close url
    del sp[0:2]
    if sp != []:
        templist.extend(sp) #Merge list

for sp in templist: #Transform temp list data into SPdatalist
    start = sp.find('\"')
    while start != -1:
        end = sp.find('\"',start+1)
        sp = sp[:start] + sp[start+1:end].replace(",","") + sp[end+1:]
        start = sp.find('\"')
    SPdatalist.append(sp)

print "part1 complete!"

for i in range(len(SPdatalist)-1):  #graph 
    sp = SPdatalist[i]
    temp = [idx for (idx, s) in enumerate(sp) if s == ',']
    tempsph =[]   
    if spdate == []:   #initial first day
        for x in range(4):
            tempsph.append(sp[temp[x + 2]+1:temp[x + 3]])
        spdate.append(sp[:temp[0]])    #record date
        sph.append(max(tempsph))
    else:
        for x in range(4):
            tempsph.append(sp[temp[x + 2]+1:temp[x + 3]])        
        if max(tempsph) > linepoint_high and min(tempsph) < linepoint_low:
            spdate.append(sp[:temp[0]]) #record date
            spdate.append(sp[:temp[0]])            
            if sp[temp[6]+1] == "-":    #decide the direction
                sph.append(max(tempsph))
                sph.append(min(tempsph))
            else:
                sph.append(min(tempsph))
                sph.append(max(tempsph))
        else:
            if max(tempsph) > linepoint_high:
                sph.append(max(tempsph))
                spdate.append(sp[:temp[0]])
            else:
                if min(tempsph) < linepoint_low:
                    sph.append(min(tempsph))
                    spdate.append(sp[:temp[0]])
    linepoint_high = max(tempsph)
    linepoint_low = min(tempsph)

print "part2a complete!"

spdatex =[]            
for i in range(len(spdate)):
    spdatex.append(i)
print len(spdatex)

plt.plot(spdatex,sph)
plt.xlim(1,len(spdatex))
plt.ylim(1,max(sph))
plt.show()
print "part3 complete!"