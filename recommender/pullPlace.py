import Place
import Checkin

def pullPl(db):
    allPlaces=set([])
    for i in db.find():
        tempCheck=Checkin(i['user'],i['venue'])
        flagged=true
        for place in places:
            if (tempCheck.getPlace()==place.getPlace()):
                flagged=false
                if (tempCheck.getUser()!=place.getUser()):
                    place.addUser(tempCheck.getUser())
                else:
                    place.dictAdd(tempCheck.getUser())
    if flagged:
        places.add(Place.Place(tempCheck.getPlace(),tempCheck.getUser))
    return places
