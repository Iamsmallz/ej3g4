# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:17:01 2013

@author: smallz
"""

import urllib

url = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAY_print.php?genpage=genpage/Report201311/201311_F3_1_8_2314.php&type=csv'  
response = urllib.urlopen(url)  
html = response.read()  
print(html.decode('cp950','ignore')) #.encode('utf-8')