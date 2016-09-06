# TO DO:
# print slice of dictionary
# sort dictionary by last name


"""
Q6. Create a dictionary in the below format:
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
"""
print '----------------- Q6. START -----------------'

import csv
import urllib2
import os
from collections import OrderedDict
from collections import defaultdict

url = 'https://raw.githubusercontent.com/th27/dsp/master/python/faculty.csv'
file_dir = '/Users/THoshino/Desktop/METIS/METISGH/PREWORK/dsp/python'
file_name = 'faculty.csv'

try:
	csv_data = urllib2.urlopen(url)	# download data from raw github url
except:
	os.chdir(file_dir)	# fall back download if no internet connection
	csv_data = open(file_name,'r')	# open file in read mode
f = csv.reader(csv_data)	# create a csv object

faculty_dict = {}
faculty_dict = defaultdict(list)
for row in f:
	key = row[0].split(' ')[-1]
	faculty_dict[key].append(row[1:])

threekv_q6 = {k:faculty_dict[k] for k in faculty_dict.keys()[:3]}
print threekv_q6

print '----------------- Q6. END -----------------'

"""
Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }"""

print '----------------- Q7. START -----------------'

os.chdir(file_dir)	# fall back download if no internet connection
csv_data = open(file_name,'r')	# open file in read mode
f = csv.reader(csv_data)	# create a csv object

professor_dict = {}
for row in f:
	key = tuple(row[0].split(' '))
	professor_dict[key] = row[1:]

threekv_q7 = {k:professor_dict[k] for k in professor_dict.keys()[:3]}
print threekv_q7

print '----------------- Q7. END -----------------'

"""
Q8. It looks like the current dictionary is printing by first name. Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors
"""

print '----------------- Q8. START -----------------'

os.chdir(file_dir)	# fall back download if no internet connection
csv_data = open(file_name,'r')	# open file in read mode
f = csv.reader(csv_data)	# create a csv object

prof_dict = {}
for row in f:
	key = tuple(row[0].split(' '))
	prof_dict[key] = row[1:]

sorted_dict = OrderedDict(sorted(prof_dict.items(), key = lambda t: t[0][-1]))
print sorted_dict

print '----------------- Q8. END -----------------'


