import unicodecsv
from datetime import datetime as time

with open('ceisve.csv', 'rb') as de:
	reader = unicodecsv.DictReader(de)
	listed = list(reader)
print listed[5]
unique = set()
for data in listed:
	unique.add(data['id'])
print len(unique)
date = '2019-01-20'
print time.strptime(date,'%Y-%m-%d')
