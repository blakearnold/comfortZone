import User
import Checkin

import Place
import pymongo
from pymongo import Connection

class AllGet:

    def __init__(this,collection):
        this.coll=collection

    def pullPl(this):
        places=set([])
        for i in this.coll.find():
            tempCheck=Checkin(i['user'],i['venue'])
            flagged=True
            for place in places:
                if (tempCheck.getPlace()==place.getPlace()):
                    flagged=False
                    if (tempCheck.getUser()!=place.getUser()):
                        place.addUser(tempCheck.getUser())
                    else:
                        place.dictAdd(tempCheck.getUser())
            if flagged:
                places.add(Place.Place(tempCheck.getPlace(),tempCheck.getUser))
        return places


    def pullUs(this):
        users=set([])
        for i in this.coll.find():
            tempCheck=Checkin(i['user'],i['venue'])
            flagged=True
            for user in users:
                if (tempCheck.getUser() == user.getUser()):
                    flagged=False
                    if (tempCheck.getPlace()!=user.getPlace()):
                        user.addPlace(tempCheck.getPlace())
                    else:
                        user.dictAdd(tempCheck.getPlace())
            if flagged:
                users.add(User.User(tempCheck.getUser(),tempCheck.getPlace()))
        return users
