import datetime
import time
from dateutil.relativedelta import relativedelta

print(datetime.datetime.now())

epoch = 1485789600

print(datetime.datetime.fromtimestamp(epoch))
#           jahr monat  tag stunde  minute sekunde msek  
birth_day = 1975,    2,  23,     4,      0,      0,   0,0,0

birth_day_dt = time.mktime(birth_day)

print(birth_day_dt)
alter = time.time() - birth_day_dt
print(alter)
print(alter/(365.25 * 24 * 3600))

dt_birth_day = datetime.date(1975,2,23)
dt_today     = datetime.date.today()

diff = dt_today - dt_birth_day
print(diff.days)
rd_age = relativedelta(dt_today, dt_birth_day)
print(rd_age.years, rd_age.months, rd_age.days)


print(dt_today + relativedelta(years=+1))


print(datetime.date(1582,10,5) + relativedelta(days=+1))
