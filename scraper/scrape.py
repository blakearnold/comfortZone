import foursquare
import pymongo
import json

f = foursquare.Api()

connection = pymongo.Connection('pureneeds.com', 27017)
db = connection.hackny
test = db.test
test.insert({'foo':'bar'})

def scrape_foursquare_user(username, password, city):
    ujson = f.get_user_detail(username, password)
    user = ujson.get('user')
    if not user: 
       return # TODO throw an error
    newuser = {}
    newuser['_id'] = user.get('id')
    db.users.insert(newuser)
    print newuser
    cjson = f.get_history(username, password, l=250)
    for checkin in cjson.get('checkins'):
        venue = checkin.get('venue')
        if not venue: 
            continue # TODO throw an error
        v_id = venue.get('id')
        newvenue = {}
        newvenue['_id'] = venue.get('id')
        newvenue['lat'] = venue.get('geolat')
        newvenue['lng'] = venue.get('geolong')
        print venue.get('city')
        db.venues.insert(newvenue)

if __name__ == "__main__":
    USERNAME = "bludman@gmail.com"
    PASSWORD = "hackny"
    CITY = "New York"
    scrape_foursquare_user(USERNAME, PASSWORD, CITY)
