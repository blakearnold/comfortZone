import User
import Checkin

def pullUs(db):
    users=set([])
    for i in db.find():
        tempCheck=Checkin(i['user'],i['venue'])
        flagged=true
        for user in users:
            if (tempCheck.getUser() == user.getUser()):
                flagged=false
                if (tempCheck.getPlace()!=user.getPlace()):
                    user.addPlace(tempCheck.getPlace())
                else:
                    user.dictAdd(tempCheck.getPlace())
    if flagged:
        users.add(User.User(tempCheck.getUser(),tempCheck.getPlace()))
    return users
