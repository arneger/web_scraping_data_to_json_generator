import re
import urllib.request
import json

hib_mandagN = "mandag_hib"
mandag_hib = [urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/208N2'), #HIB Lille Aud
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/209M3'), #HIB Store Aud
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/205M3'), #HIB GrRom 205M3
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/208M1'), #HIB GrRom 208M1
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/209M1'), #HIB GrRom 209M1
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/209N1')  #HIB GrRom 209N1
]

hib_tirsdagN = "tirsdag_hib"
tirsdag_hib = [urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/208N2'), #HIB Lille Aud
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/209M3'), #HIB Store Aud
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/106O1'), #HIB Datalab 1
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/105O1'), #HIB Datalab 2
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/104O1')] #HIB Datalab 3

hib_onsdagN = "onsdag_hib"
onsdag_hib = [urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/208N2'), #HIB Lille Aud
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/209M3'), #HIB Store Aud
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/357/208'), #VilVite Konf A
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/357/209'), #VilVite Konf B
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/357/216'), #VilVite Konf C
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/357/206')] #VilVite Konf D

hib_torsdagN = "torsdag_hib"
torsdag_hib = [urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/208N2'), #HIB Lille Aud
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/209M3'), #HIB Store Aud
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/106O1'), #HIB Datalab 1
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/105O1'), #HIB Datalab 2
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/104O1')] #HIB Datalab 3

hib_fredagN = "fredag_hib"
fredag_hib = [urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/208N2'), #HIB Lille Aud
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/209M3'), #HIB Store Aud
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/205M3'), #HIB GrRom 205M3
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/208M1'), #HIB GrRom 208M1
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/209M1'), #HIB GrRom 209M1
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/351/209N1')]  #HIB GrRom 209N1

rfb_mandagN = "mandag_rfb"
mandag_rfb = [urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/315/A-114'), #A66 Aud A
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/315/A-112'), #A66 Aud B
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UC7B'), #RFB AUD1
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UC6F'), #RFB AUD2
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UA5F'), #RFB AUD3
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/4E12F'), #RFB AUD4
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/3C12A'), #RFB AUD5
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/310/234'), #A70 Foredr.sal 200
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/310/320'), #A70 320
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/1B7A'), #RFB DataLab 1002
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/1B6D'), #RFB DataLab 1003
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/309/292')]  #A55 GrRom 292

rfb_tirsdagN = "tirsdag_rfb"
tirsdag_rfb = [urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/315/A-114'), #A66 Aud A
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/315/A-112'), #A66 Aud B
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UC7B'), #RFB AUD1
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UC6F'), #RFB AUD2
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UA5F'), #RFB AUD3
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/4E12F'), #RFB AUD4
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/3C12A'), #RFB AUD5
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/310/320'), #A70 320
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/309/316'), #A55 GrRom 316
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/309/366'), #A55 GrRom 366
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/309/368'), #A55 GrRom 368
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/309/546')] #A55 GrRom 546

rfb_onsdagN = "onsdag_rfb"
onsdag_rfb = [urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/315/A-114'), #A66 Aud A
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/315/A-112'), #A66 Aud B
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UC7B'), #RFB AUD1
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UC6F'), #RFB AUD2
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UA5F'), #RFB AUD3
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/4E12F'), #RFB AUD4
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/3C12A'), #RFB AUD5
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/310/320'), #A70 320
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/2C11D'), #RFB GlassBuret
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UA7B'), #RFB GR-Rom 6
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/2A1F'), #RFB GR.Rom sp2
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/1F9D')] #RFB Aktiv Læring

rfb_torsdagN = "torsdag_rfb"
torsdag_rfb = [urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/315/A-114'), #A66 Aud A
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/315/A-112'), #A66 Aud B
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UC7B'), #RFB AUD1
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UC6F'), #RFB AUD2
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UA5F'), #RFB AUD3
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/4E12F'), #RFB AUD4
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/3C12A'), #RFB AUD5
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/310/320'), #A70 320
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/1D5D'), #RFB SEM 2
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/4E15B'), #RFB Pi i fjerde
               urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/3F4C')] #RFB Tripletten

rfb_fredagN = "fredag_rfb"
fredag_rfb = [urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/315/A-114'), #A66 Aud A
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/315/A-112'), #A66 Aud B
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UC7B'), #RFB AUD1
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UC6F'), #RFB AUD2
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/UA5F'), #RFB AUD3
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/4E12F'), #RFB AUD4
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/3C12A'), #RFB AUD5
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/310/234'), #A70 foredr.sal 200
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/310/320'), #A70 320
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/1B7A'), #RFB DataLab 1002
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/1B6D'), #RFB DataLab 1003
              urllib.request.urlopen('http://dagstavle.app.uib.no/q.php/308/1F9D')] #RFB Aktiv Læring

def json_generator(the_pages, dagen):
    # Gathers booking, building and room information from each room
    rfb_datetime_dict = {}
    for page in the_pages:
        html = page.read()
        html_output = html.decode('utf-8')

        # Finds the content (building and room) inside the h1 tag.
        h1_content = re.findall(r'<h1>.*?</h1>', html_output)
        h1_building = re.findall(r'">.*?<!', h1_content[0])
        building_name = re.sub(r'.*?">|<!', '', h1_building[0])  # Building
        h1_room = re.findall(r'>:.*?<!', h1_content[0])
        room_name = re.sub(r'>:.*?">|<!|>:', '', h1_room[0])  # Room

        # Finds information about when room is booked
        td_time = re.findall(r'<td class.*?</td>', html_output)
        join_td_time = " ".join(td_time)
        dateTime_content = re.findall(r'time datetime=.*?</time>', join_td_time)
        temp_dateTime_list = []
        for dateAndTime in dateTime_content:
            dateTime = re.sub(r'.*?time datetime="|</time>|T|">', ' ', dateAndTime)
            temp_dateTime_list.append(dateTime.split()[:-1])

        # Creates a readable structure of the lists (values) that'll be in rfb_datetime_dict
        dates_from_to = []
        col_index = 0
        for eachDateTime in temp_dateTime_list:
            if col_index % 2 != 0:
                try:
                    dates_from_to[col_index - 2] += eachDateTime
                except:
                    dates_from_to[-1] += eachDateTime
            else:
                dates_from_to.append(eachDateTime)
            col_index += 1
        for time_info in dates_from_to:
            del time_info[-2]

        # Creates a dictionary with building+room as key and the list(s) with date, from, to as value.
        rfb_datetime_dict[building_name + " " + room_name] = dates_from_to # value: 0=dato, 1=fra, 2=til

    # creates json file from rfb_date_dict.
    with open(dagen+".json", "w") as file:
        file.write(json.dumps(rfb_datetime_dict, indent=2)) #fjern indent for å fjerne newline i json


def main():
    #Note: Make the arguments as inputs so it's easier for others to use the code.
    #Meanwhile, just change the arguments to choose day.
    json_generator(onsdag_rfb, rfb_onsdagN)
    plan_saved = json.load(open(rfb_onsdagN+".json", "r"))
    for key, value in plan_saved.items():
        print(key, "    :    ", value)
if __name__ == "__main__":
    main()

