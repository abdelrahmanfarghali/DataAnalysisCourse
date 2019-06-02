import unicodecsv
from collections import defaultdict
import numpy as np
from datetime import datetime as time
import matplotlib.pyplot as plt

with open('ceisve.csv', 'rb') as de:
	reader = unicodecsv.DictReader(de)
	listed = list(reader)
print listed[5]
unique = set()
for data in listed:
	unique.add(data['id'])
print len(unique)
date = '2019-01-20'
datsa = []
print time.strptime(date,'%Y-%m-%d')
for total_minutes in listed:
	datsa.append(total_minutes['permissions'])
print np.mean({'a':5,'b':5,'c':5}.values())
print np.std({'a':5,'b':5,'c':5}.values())
print np.max({'a':5,'b':5,'c':5}.values())
print np.min({'a':5,'b':5,'c':5}.values())
{'a':5,'b':5,'c':5}.items()
#time_delta = date - (date + 5)
#if time_delta.days < 7:
#	print 'H'
plt.hist([5,3,6,7,8,10,22],bins=3)
plt.ylabel('Y')
plt.xlabel('X')
plt.title('The World')
plt.show()
