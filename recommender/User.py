class User:
    
    def __init__(self, places):
        self.places = places
    
    def getPlaces(self):
        return self.places
    
    def addPlace(self, place):
        self.places.add(place)
    
    def setPlaces(self, places):
        self.places = places