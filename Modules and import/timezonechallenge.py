import pytz
import datetime

menu = pytz.all_timezones[:9]

print("available time zones are ")
for x in menu:
    print(x)
selection = int(input("Please choose any one of the timezone or 0 to quit"))
if selection:
    selected = menu[selection-1]
    tzer = pytz.timezone(selected)
    localtime = datetime.datetime.astimezone(tzer)
    print(localtime)
else:
    print("quitt")

