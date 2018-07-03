import time

print(time.daylight) ## if daylight returns 1 use the second string in tzname

print(time.timezone) ## timezone returns the offset from UTC and it uses non DST

print(time.tzname) ## returns a tuple containing two strings name of the
#non dst timezone and also the name of the dst timezone

if time.daylight:
    print(time.tzname[1])
else:
    print(time.tzname[0])

print("local time is " + time.strftime("%Y-%m-%d  %H:%M:%I",time.localtime()))
print("UTC time is " + time.strftime("%Y-%m-%d  %H:%M:%I",time.gmtime()))