import urllib2
from BeautifulSoup import *
import re
import xlrd

#get the contents of the page...
#TODO: get list of urls from sara
#read excel file
def read_workbook():
    '''This function reads in the rows of a workbook and returns the value'''
    wb = xlrd.open_workbook('/home/cody/Desktop/master.xls')
    wb.sheet_names()
    sh = wb.sheet_by_index(0)
    #keep a list of the urls
    url_list = []
    for rownum in range (sh.nrows):
        rowval = sh.cell_value(rownum, 0)
        url_list.append(rowval)
        i = 1
    while i <= len(url_list):
        return str(url_list[i])
        i += 1
        
'''
#get the soup
soup = BeautifulSoup(html)
x = soup.findAll('script')
y = len(x)
count = 0
#find the code
for i in range(y):
    string = str(x[i])
    adbull = string.find('adbull')
    #if found, replace the script tags with nothing... (so it prints prettier)
    if adbull != -1:
        extracted = string.replace('<script src="', '')
        final_url = extracted.replace('"></script>', '')
        print final_url
        count += 1
if count < 1:
    print "Invocation Code Not Found."
else:
    print "Invocation Code Search Successful"
'''
