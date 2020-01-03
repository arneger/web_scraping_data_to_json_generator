from datetime import datetime, timedelta
import json
import jsonFromHTMLGenerator

nowtime = datetime.now()
current_year = nowtime.year
current_month = nowtime.month
current_day = nowtime.day
current_hour = nowtime.hour
current_minute = nowtime.minute
openRoom = ["Ledig resten av dagen"]

#Choose which json to open. Optionally add an input variable to do this in console.
plan_saved2= json.load(open("onsdag_rfb"+".json", "r"))

hours = (datetime(current_year, current_month, current_day, 8), datetime(current_year, current_month, current_day, 18))

booking_hours = {}
for key, value in plan_saved2.items():
    romnavn = key
    booking_hours[romnavn] = []
    listen = []
    if value == []:
        booking_hours[romnavn] = openRoom
        continue
    for x in value:
        fraTime = int(x[1][0:2])
        fraMin = int(x[1][3:5])
        tilTime = int(x[2][0:2])
        tilMin = int(x[2][3:5])
        listen.append((datetime(current_year, current_month, current_day, fraTime, fraMin), datetime(current_year, current_month, current_day, tilTime, tilMin)))

    duration = timedelta(hours=0.02)
    slots = sorted([(hours[0], hours[0])] + listen + [(hours[1], hours[1])])
    for start, end in ((slots[i][1], slots[i + 1][0]) for i in range(len(slots) - 1)):
        while start + duration <= end:
            booking_hours[romnavn] += ["{:%H:%M}-{:%H:%M}".format(start, start + duration)]
            start += duration

dicto = {}
for key, value in booking_hours.items():
    if value == openRoom:
        dicto[key] = [openRoom]
        continue
    value = [x.split("-") for x in value]
    navn = key
    final = []
    templist = []
    for x in value:
        if templist == []:
            templist.append(x)
        if x[0] == templist[-1][1]:
            templist[-1][1] = x[1]
            try:
                if value[value.index(x) + 1][0] != templist[-1][1]:
                    final += templist
                    templist = []
            except:
                final += templist
    dicto[navn] = final

for key, value in dicto.items():
    for x in value:
        if x == openRoom:
            continue
        fra = x[0][0:2]
        mfra = x[0][3:5]
        til = x[1][0:2]
        mtil = x[1][3:5]
        if fra.startswith("0"):
            fra = fra[1]
        if til.startswith("0"):
            til = til[1]
        if int(fra) < int(current_hour) and int(til) < int(current_hour):
            value.remove(x)
    if value == []:
        value = [openRoom]


for key, value in dicto.items():
    print(key,"\n", value, "\n")
