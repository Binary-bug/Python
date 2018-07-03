import pytz
import datetime
import random

menu=list('')
for i in range(10):
    menu.append(pytz.all_timezones[random.randint(1,591)])

print("available time zones are ")
for x in menu:
    print(menu.index(x)+1,x)
while True:
    selection = int(input("Please choose any one of the timezone or 0 to quit"))
    if selection:
        selected = menu[selection-1]
        tzer = pytz.timezone(selected)
        localtime = datetime.datetime.now(tz=tzer)
        print("The time in {} is {} {}".format(selected,localtime.strftime("%A %x %X %z"),localtime.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime("%A %x %X")))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime("%A %x %X")))
    else:
        print("quitting")
        break

