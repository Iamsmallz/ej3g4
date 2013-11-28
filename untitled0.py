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
        
    def ymdatelist(self): #get all year & month value

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
    
    def now(self):
        
        if self.nowmonth >= 10:
            return str(self.nowyear) + str(self.nowmonth)
        else:
            return str(self.nowyear) + '0' + str(self.nowmonth)
                     


snumber = '2314'
SPdatalist = []
templist = []
spdate = []
sph = []
SDatelist = SDate()
SDatelist.ymdatelist()

if os.path.exists('s_' + snumber +'.txt'):    #open old file
    file = open('s_' + snumber +'.txt')
    line = file.readline()
    while len(line) != 0:
        SPdatalist.append(line)
        line = file.readline() #next line
    file.close()
    PastPricemark = SPdatalist[len(SPdatalist)-1] #get the last one item
else:
    PastPricemark = ' 82/01/04,0,0,0,0,0,0,0,0'
    
s = PastPricemark[:PastPricemark.find(',')].find('/')   #get the date in the last one item
PastPricemarkDate = str(int(PastPricemark[:s])+1911) + PastPricemark[s+1:s+3]

if PastPricemarkDate == SDatelist.now():
    url = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAY_print.php?genpage=genpage/Report' \
    + SDatelist.now() + '/' + SDatelist.now() +'_F3_1_8_' + snumber + '.php&type=csv'
    templist = urllib.urlopen(url).read().splitlines()
    
    for z in range(len(templist)):
        if templist[z].find('\xbc\xc6') > 0:
            break
    del templist[0:z+1]
    
    for i in range(len(templist)):
        p = templist[i]
        if p[:templist[i].find(',')] == PastPricemark[:PastPricemark.find(',')]:
            break
    p = templist[i+1:]
    if p != []:
        for sp in p:
            start = sp.find('\"')
            while start != -1:
                end = sp.find('\"',start+1)
                sp = sp[:start] + sp[start+1:end].replace(",","") + sp[end+1:]
                start = sp.find('\"')
            SPdatalist.append(sp+'\n')       
else:
    for i in range(len(SDatelist.SD)):
        if (str(int(PastPricemark[:s])+1911) + PastPricemark[s+1:s+3]) == SDatelist.SD[i]:
            break
        
    for x in SDatelist.SD[i:]:
        
        url = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAY_print.php?genpage=genpage/Report' \
        + x + '/' + x +'_F3_1_8_' + snumber + '.php&type=csv'
        templist = urllib.urlopen(url).read().splitlines()
        
        for z in range(len(templist)):
            if templist[z].find('\xbc\xc6') > 0:
                break
        del templist[0:z+1]
        
        if PastPricemarkDate == x:
            for y in range(len(templist)):
                p = templist[y]
                if p[:templist[y].find(',')] == PastPricemark[:PastPricemark.find(',')]:
                    break
            p = templist[y+1:]
            if p != []:
                for sp in p:
                    start = sp.find('\"')
                    while start != -1:
                        end = sp.find('\"',start+1)
                        sp = sp[:start] + sp[start+1:end].replace(",","") + sp[end+1:]
                        start = sp.find('\"')
                    SPdatalist.append(sp+'\n')                
        else:
            for sp in templist:
                start = sp.find('\"')
                while start != -1:
                    end = sp.find('\"',start+1)
                    sp = sp[:start] + sp[start+1:end].replace(",","") + sp[end+1:]
                    start = sp.find('\"')
                SPdatalist.append(sp+'\n')
              
if os.path.exists('s_' + snumber +'.txt'):
    os.remove('s_' + snumber +'.txt')

file = open('s_' + snumber +'.txt', 'w')
for i in range(len(SPdatalist)):
    line = str(SPdatalist[i])
    file.write(line)
file.close()        

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
            tempsph.append(sp[temp[x + 2]+1:temp[x + 3]])      #graph rule  
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

plt.plot(spdatex,sph)
plt.xlim(1,len(spdatex))
plt.ylim(1,max(sph))
plt.show()
print "part3 complete!"