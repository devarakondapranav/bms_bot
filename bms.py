import time, datetime
from bs4 import BeautifulSoup
import http.cookiejar
import urllib

import os

bms_2d_rrr_url = "https://in.bookmyshow.com/buytickets/rrr-hyderabad/movie-hyd-ET00094579-MT/20220325"
def getVenues():
    try:
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)
        data = urllib.parse.urlencode({}).encode('utf-8')
        req = urllib.request.Request(bms_2d_rrr_url, data, headers={'User-Agent': 'Chrome'})
        resp = urllib.request.urlopen(req)
        resp_data = resp.read()

        soup = BeautifulSoup(resp_data)
        venues = soup.find_all("a", {"class":"__venue-name"})
        return venues

    except Exception as msg:
        print(msg)

def updateMap(venues, venueMap):

    venueMap = {}

    for venue in venues:
        venueMap[venue.text.strip()] = True
    return venueMap


venueMap = {}
while(True):
    time.sleep(3)
    venues = getVenues()
    venue_count = len(venues)
    print(str(venue_count) + " theatres open at " + str(datetime.datetime.now()))
    newTheatre = False
    for venue in venues:
        if venue.text.strip() not in venueMap:
            newTheatre = True
            venueMap[venue.text.strip()] = True
            print("******************************* " + venue.text.strip() + " newly added")
    venueMap = updateMap(venues, venueMap)


    if(newTheatre):
        os.startfile("D:\\laptop_data\\code\\bot\\inka_edo.mp3")

