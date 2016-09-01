import csv
import urllib2

url = 'https://raw.githubusercontent.com/thisismetis/dsp/master/python/football.csv'
csv_data = urllib2.urlopen(url)
data = csv.reader(csv_data)

goals = []
for x in data:
	goals.append(x[5])
goals.pop(0)
# print goals

url = 'https://raw.githubusercontent.com/thisismetis/dsp/master/python/football.csv'
csv_data = urllib2.urlopen(url)
data = csv.reader(csv_data)

goals_allowed = []
for x in data:
	goals_allowed.append(x[6])
goals_allowed.pop(0)
# print goals_allowed

diff = [int(x) - int(y) for x, y in zip(goals, goals_allowed)]
team_index = diff.index(min(diff))
# print team_index

url = 'https://raw.githubusercontent.com/thisismetis/dsp/master/python/football.csv'
csv_data = urllib2.urlopen(url)
data = csv.reader(csv_data)

teams = [x[0] for x in data]
team = teams[team_index + 1]
print team
