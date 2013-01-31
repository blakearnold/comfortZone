#just for checkins, only getter uses this

class Checkin:
    def __init__(self,user,place):
        self.user=user
        self.place=place

    def getUser(self):
        return self.user

    def getPlace(self):
        return self.place
