## converting UTC to local time is fairly easy but reverse is not so

import datetime
import pytz

localtime = datetime.datetime.now()
utctime = datetime.datetime.utcnow()

print("Naive localtime is {}:".format(localtime))

print("Naive UTC time is {}:".format(utctime))


## converting it to an aware time using pytz module , always work with utctime

aware_localtime = pytz.utc.localize(utctime).astimezone() # defaulted to the local timezone
print("aware local time {}, using timezone {}:".format(aware_localtime,aware_localtime.tzinfo))

aware_utctime = pytz.utc.localize(utctime)
print("aware utc time {}, timezone {}:".format(aware_utctime,aware_utctime.tzinfo))

#timestamp

gaptime = datetime.datetime(2015,10,25,1,30,0,0)
print(gaptime)
print(gaptime.timestamp())

s = 1445733000

t = s + (60*60)  ## adding an hour

gb = pytz.timezone('GB') # creating tzinfo object

dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s,dt1))

print("{} seconds since the epoch is {}".format(t,dt2))