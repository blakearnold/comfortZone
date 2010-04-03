class Place:
    
    def __init__(self, place, users):
        self.users = set([users])
        self.place = place
        self.dict={user : 1}
    
    def addUser(self, user):
        self.users.add(user)

    def dictAdd(self, user):
        self.dict[user]=self.dict[user]+1
    
    def setUsers(self, users):
        self.users = users
        
    def getUsers(self):
        return self.users
    
    def getNum(self,user):
        return self[user]

    def getPlace(self):
        return self.place
