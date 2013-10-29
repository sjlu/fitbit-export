__author__ = "sjlu"

import fitbit
import datetime
import json

# Initializing Fitbit client
fitbit_key = '64444929be02417abc8817870556c687'
fitbit_secret = '6f55521cb295436c9008f1c95bc12469'
user_key = '6c0621b4d31b711e9b1198435d8e51d7'
user_secret = 'aa6996b75ab32b871c20cb0db47b7ff5'
fitbit_client = fitbit.Fitbit(fitbit_key, fitbit_secret, user_key=user_key, user_secret=user_secret, system='en_US')

asleep = fitbit_client.make_request('http://api.fitbit.com/1/user/-/sleep/minutesAsleep/date/today/max.json')
consumed = fitbit_client.make_request('http://api.fitbit.com/1/user/-/foods/log/caloriesIn/date/today/max.json')
burned = fitbit_client.make_request('http://api.fitbit.com/1/user/-/activities/calories/date/today/max.json')
weight = fitbit_client.make_request('http://api.fitbit.com/1/user/-/body/weight/date/today/max.json')
fat = fitbit_client.make_request('http://api.fitbit.com/1/user/-/body/fat/date/today/max.json')

days = {}
def iterate(key, array):
  for item in array[key]:
    day = str(item['dateTime'])
    value = item['value']
    if not days.get(day):
      days[day] = {}
    days[day][key] = value

iterate('body-weight', weight)
iterate('body-fat', fat)
iterate('activities-calories', burned)
iterate('foods-log-caloriesIn', consumed)
iterate('sleep-minutesAsleep', asleep)

output = []
for k,v in days.iteritems():
  v['date'] = k;
  output.append(v)

output = sorted(output, key=lambda x: x['date'])

print json.dumps(output, indent=2, separators=(',',': '))
