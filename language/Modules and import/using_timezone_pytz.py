import pytz
import datetime

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country) # used to create tzinfo object and localtime in line 7 is using it
localtime = datetime.datetime.now(tz=tz_to_display)
print('The time in {} is {}'.format(country,localtime))
print('UTC is {}'.format(datetime.datetime.utcnow()))

# for x in pytz.all_timezones:
#     print(x)  ## to get a list of # all pytz timezones

## alsoo we can use country codes pytz.country_names is a dictionary

for x in sorted(pytz.country_names):
    print(x + ":" + pytz.country_names[x])


# country names are not good enough though, since each country can possibly have
# multiple timezones


# without get this might throw an error if there are countries with no timezones

for x in sorted(pytz.country_names):
    print("{}: {}: {}:".format(x,pytz.country_names[x],pytz.country_timezones.get(x)))

## to avoid None by using get
print('X'*100)
for x in sorted(pytz.country_names):
    print("{}: {}".format(x,pytz.country_names[x]),end=':')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            print("\t\t{}: {} ".format(zone,datetime.datetime.now(tz=pytz.timezone(zone))))
    else:
        print('\t\tNo timezone defined')

