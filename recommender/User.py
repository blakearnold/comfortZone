#user
#has a dictionary to hold the number of times the user has visited each place
#has a user to identify itself
#has a set of places to know the user has gone.


#NEEDS TO BE CHANGED SO DICTIONARIES ARE USEFUL
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

