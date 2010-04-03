class User:
    
    def __init__(self, user, place):
        self.places = set([place])
        self.user = user
        self.dict={place:1}
    
    def getPlaces(self):
        return self.places

    def dictAdd(self, place):
        self.dict[place]=self.dict[place]+1

    def getUser(self):
        return self.user
    
    def addPlace(self, place):
        self.places.add(place)
        self.dict[place]=1
    
    def setPlaces(self, places):
        self.places = places

    def getNum(self,place):
        return self.dict[place]

