# @ Reshama - solution is naive so I will come back to refine
# TO DO:
# split into functions
# split string in list where multiple degrees
# use regex to identify same degrees expressed differently

import csv
import urllib2
import re
import os

url = 'https://raw.githubusercontent.com/th27/dsp/master/python/faculty.csv'
file_dir = '/Users/THoshino/Desktop/METIS/METISGH/PREWORK/dsp/python'
file_name = 'faculty.csv'

"""
Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
"""

print '----------------- Q1. START -----------------'

try:
	csv_data = urllib2.urlopen(url)	# download data from raw github url
except:
	os.chdir(file_dir)	# fall back download if no internet connection
	csv_data = open(file_name,'r')	# open file in read mode
f = csv.reader(csv_data)	# create a csv object
degree = []	# empty list
for i in f:
	degree.append(i[1])	# add individual lines as strings to new list
degree.pop(0)	# remove column header

s = ', '.join(degree)	# create single string to run regex findall across all degrees

# regex for each degree type

re_phd = r"[Pp][Hh].?[Dd].?"
re_scd = r"[Ss][Cc].?[Dd].?"
re_md = r"[Mm].?[Dd].?"
re_mph = r"[Mm][Pp][Hh]"
re_bsed = r"[Bb].?[Ss].?[Ee].?[Dd].?"
re_ms = r"[Mm].?[Ss].?"
re_jd = r"[Jj].?[Dd].?"
re_ma = r"[Mm].?[Aa].?"

# count of each degree type

print "There are %d academic/s with a Ph.D" % len(re.findall(re_phd, s))
print "There are %d academic/s with a Sc.D" % len(re.findall(re_scd, s))
print "There are %d academic/s with a M.D." % len(re.findall(re_md, s))
print "There are %d academic/s with a MPH" % len(re.findall(re_mph, s))
print "There are %d academic/s with a B.S.Ed" % len(re.findall(re_bsed, s))
print "There are %d academic/s with a M.S" % len(re.findall(re_ms, s))
print "There are %d academic/s with a J.D" % len(re.findall(re_jd, s))
print "There are %d academic/s with a M.A" % len(re.findall(re_ma, s))

print '----------------- Q1. END -----------------'

"""
Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
"""

# @ Reshama - solution is naive so I will come back to refine
# TO DO:
# not able to discern 'Assistant Professor of Biostatistics'

print '----------------- Q2. START -----------------'

try:
	csv_data = urllib2.urlopen(url)	# download data from raw github url
except:
	os.chdir(file_dir)	# fall back download if no internet connection
	csv_data = open(file_name,'r')	# open file in read mode
f = csv.reader(csv_data)	# create a csv object
titles = []	# empty list
for i in f:
	titles.append(i[2])	# add individual lines as strings to new list
titles.pop(0)	# remove column header
t_set = set(titles)
print 'There are %d different titles' % len(t_set)

# regex for each degree type

d = dict()
for title in titles:
	if title not in d:
		d[title] = 1
	else:
		d[title] += 1
for entry in d:
	print entry, d[entry]

print '----------------- Q2. END -----------------'

"""
Q3. Search for email addresses and put them in a list. Print the list of email addresses.
"""

print '----------------- Q3. START -----------------'

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
print emails

print '----------------- Q3. END -----------------'

"""
Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, 
email.chop.edu, etc.). Print the list of unique email domains.
"""

print '----------------- Q4. START -----------------'

s = ', '.join(emails)
match = re.findall(r"@([\w.-]+)", s)
set_match = set(match)
print len(set_match)
print set_match

print '----------------- Q4. END -----------------'



