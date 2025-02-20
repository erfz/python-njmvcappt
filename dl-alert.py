import urllib.request
import re
import time
from bs4 import BeautifulSoup
from datetime import datetime
import winsound

location_arr = [
    "232",
    "233",
    "235",
    "254",
    "237",
    "238",
    "240",
    "241",
    "243",
    "244",
    "246",
    "247",
    "249",
    "250",
    "252",
    "253",
    "234",
    "236",
    "239",
    "242",
    "245",
    "248",
    "251",
]
locationname_arr = [
    "Bakers Basin",
    "Bayonne",
    "Camden",
    "Cardiff",
    "Delanco",
    "Eatontown",
    "Edison",
    "Flemington",
    "Freehold",
    "Lodi",
    "Newark",
    "North Bergen",
    "Oakland",
    "Paterson",
    "Rahway",
    "Randolph",
    "Rio Grande",
    "Salem",
    "South Plainfield",
    "Toms River",
    "Vineland",
    "Wayne",
    "West Deptford",
]
base_url_link = "https://telegov.njportal.com/njmvc/AppointmentWizard/17/"
required_months = ["August"]


def beep():
    winsound.Beep(1500, 500)
    winsound.Beep(4500, 500)
    winsound.Beep(2500, 500)
    winsound.Beep(1500, 500)
    winsound.Beep(4500, 500)
    winsound.Beep(2500, 500)


def job():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n\n\nDate Time: ", dt_string, "\n\n")
    i = 0
    found = 0

    for location in location_arr:
        print(location)
        with urllib.request.urlopen(base_url_link + location) as response:
            page_html = response.read()
        soup = BeautifulSoup(page_html, "lxml")
        unavailable = soup.find("div", attrs={"class": "alert-danger"})
        if unavailable is not None:
            # print('No appointments are available in '+locationname_arr[i])
            dt_string = ""
        else:
            dates_html = soup.find("div", attrs={"class": "col-md-8"})
            date_string = dates_html.find("label", attrs={"class": "control-label"})
            if set(required_months) & set(date_string.text.split()):
                # print("Matching required months")
                date_string = re.sub("Time of Appointment for ", "", date_string.text)
                date_string = re.sub(":", "", date_string)
                message = (
                    "DL Renew Dates: "
                    + locationname_arr[i]
                    + " / ("
                    + location
                    + ") : "
                    + date_string
                )
                print(message)
                beep()
                found = 1
        i = i + 1


while True:
    try:
        job()
    except:
        print("Something went wrong")
        time.sleep(60)
    else:
        time.sleep(60)
