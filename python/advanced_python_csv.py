# TO DO:
# currently outputting into contiguous columns
# update so that it outputs in new rows

import csv
import urllib2
import re
import os

url = 'https://raw.githubusercontent.com/th27/dsp/master/python/faculty.csv'
file_dir = '/Users/THoshino/Desktop/METIS/METISGH/PREWORK/dsp/python'
file_name = 'faculty.csv'

try:
	csv_data = urllib2.urlopen(url)	# download data from raw github url
except:
	os.chdir(file_dir)	# fall back download if no internet connection
	csv_data = open(file_name,'r')	# open file in read mode
f = csv.reader(csv_data)	# create a csv object
emails = []	# empty list
for i in f:
	emails.append(i[3])	# add individual lines as strings to new list
emails.pop(0)	# remove column header

resultfile = open('emails.csv', 'wb')
wr = csv.writer(resultfile, dialect = 'excel')
for email in emails:
	wr.writerow([email])