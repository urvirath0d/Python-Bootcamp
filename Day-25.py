
from datetime import datetime, date, timedelta
date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)
dt = date.today() - timedelta(5)
print('Current Date :', date.today())
print('5 days before Current Date :', dt)
dt = date.today()
print(datetime.combine(dt, datetime.min.time()))
import datetime

base = datetime.datetime.today()
for x in range(0, 7):
    print(base + datetime.timedelta(days=x))
