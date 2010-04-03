class RecommendationEngine:

    global PLACES
    global USERS
    
    #allPlaces are in home zone
    #PLACES is number of places to find
    #USERS is number of other users to find
    def runRec(self, PLACES, USERS, allPlaces):
        self.PLACES = PLACES
        self.USERS = USERS        
        topPlaces = self.setPlaces(allPlaces)
        topPlaceUsers = self.setTopPlaceUsers(topPlaces)
        topUsers = self.setTopUsers(topPlaceUsers, allPlaces)
        self.getVisitable(topUsers, allPlaces)
        
    
    def getVisitable(self, users, allPlaces):
        userPlaces = set([])
        for i in users :
            for j in i.getPlaces():
                userPlaces.add(j)
        return userPlaces - allPlaces
    
    def setTopUsers(self, topPlaceUsers, places):
        userKeys = {}
        for i in topPlaceUsers :
            userKeys[i] =  1.0*len(i.getPlaces() & places)/len(i.getPlaces()|places)
            #makes the key based on the jaccard index
        topUsers = set([])
        for i in topPlaceUsers :
            if len(topUsers) < USERS :
                topUsers.add(i)
            else :
                if self.isLarger(userKeys[i], userKeys, topUsers) :  #checks if elt is larger than all of the elts in topUsers
                    topUsers.remove(self.findSmallest(userKeys, topUsers)) #if it is, remove that crappy one and add new one
                    topUsers.add(i)
        return topUsers
    
    def findSmallestKey(self, myKeys, myUsers):
        smallNum = 50000
        smallElt = None
        for i in myUsers :
            if smallNum > myKeys[i] :
                smallElt = i
                smallNum=myKeys[i]
        return  smallElt
    
    def keyLarger(self, currentNum, userKeys, topUsers):
        isLarger = False
        for currentKey in topUsers :
            if (userKeys[currentKey] > currentNum) :
                isLarger = True
        return isLarger
    
    #gets all users associated with passed set of places
    def setTopPlaceUsers(self, places):
        topUsers = set([])
        for i in places :
            for j in i.getUsers():
                topUsers.add(j)
        return topUsers
    
    #gets top places
    def setPlaces(self, allPlaces):
        places = set([])
        for i in allPlaces :
            if len(allPlaces) > PLACES :
                places.add(i)
            else :
                if self.isLarger(i, places) :
                    places.remove(self.findSmallest(places)) 
                    places.add(allPlaces[i])
        return places
    
    def isLarger(self, currentPlace, places):
        isLarger = False
        for j in places :
            if (currentPlace.getNum() > j.getNum()) :
                isLarger = True
        return isLarger
    
    def findSmallest(self, mySet):
        smallNum = 50000
        smallElt = None
        for i in mySet :
            if smallNum > i.getNum() :
                smallElt = i
                smallNum = i.getNum()
        return  smallElt
