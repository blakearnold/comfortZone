import User
import Checkin

import Place
import pymongo
from pymongo import Connection

#I don't know if this is broken or not.

class AllGet:

#this is where my trouble started
    def __init__(this,collection):
        this.coll=collection
        this.places=set([])
        this.users=set([])
        for i in this.coll.find():
            tempCheck=Checkin(i['user'],i['venue'])
            flagged=True
            #the idea is to make sure everyone gets the same objects.
            #I don't know if this way of passing objects makes them all the same
            #but theoretically they are.
            for place in this.places:
                if (tempCheck.getPlace()==place.getPlace()):
                    flagged=False
                    if (tempCheck.getUser()!=place.getUser()):
                        place.addUser(tempCheck.getUser())
                    else:
                        place.dictAdd(tempCheck.getUser())
            if flagged:
                this.places.add(Place.Place(tempCheck.getPlace(),tempCheck.getUser))
            tempCheck=Checkin(i['user'],i['venue'])
            flagged=True
            for user in this.users:
                if (tempCheck.getUser() == user.getUser()):
                    flagged=False
                    if (tempCheck.getPlace()!=user.getPlace()):
                        user.addPlace(tempCheck.getPlace())
                    else:
                        user.dictAdd(tempCheck.getPlace())
            if flagged:
                this.users.add(User.User(tempCheck.getUser(),tempCheck.getPlace()))

    def pullPl(this):
            return this.places

    def pullUs(this):
            return this.users

#the following was my old code, but I realized that the users and places that
#each set was dealing with was different.  I don't know if this solves my
#problem.
'''    def pullPl(this):
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
'''
