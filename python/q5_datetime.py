# Hint:  use Google to find python function

from datetime import date

def diff_dates(date_start, date_stop):
	return abs(date_stop - date_start).days

####a) 
# date_start = '01-02-2013'  
# date_stop = '07-28-2015'   

date_start = date(2013,1,2)
date_stop = date(2015,7,28)
print "%d days difference" % diff_dates(date_start,date_stop)   

####b)  
# date_start = '12312013'  
# date_stop = '05282015'  

date_start = date(2013,12,31)
date_stop = date(2015,5,28)
print "%d days difference" % diff_dates(date_start,date_stop)   

####c)  
# date_start = '15-Jan-1994'  
# date_stop = '14-Jul-2015'  

date_start = date(1994,1,15)
date_stop = date(2015,7,14)
print "%d days difference" % diff_dates(date_start,date_stop)   
