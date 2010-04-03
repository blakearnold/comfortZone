class Place:
    
    def __init__(self, users, checkins):
        self.users = users
        self.num = checkins
    
    def addUser(self, user):
        self.users.add(user)
    
    def setUsers(self, users):
        self.users = users
        
    def setNum(self, number):
        self.num, number
    
    def getUsers(self):
        return self.users
    
    def getNum(self):
        return self.num