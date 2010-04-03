import User
import Place
import RecommendationEngine
import pymongo
from pymongo import Connection
#connection = Connection()
#connection = Connection('pureneeds.com', 27017)
#db = connection.hackny
#db = connection['test-database']



r = RecommendationEngine.RecommendationEngine()
#TODO:
user1=None
user2=None
place1= Place.Place(set([user1]),1)
place2= Place.Place(set([user1,user2]),2)
user2 = User.User(place2)
user1 = User.User(place1)
allPlaces=set([place1, place2])
#print (allPlaces)
print (r.runRec(2, allPlaces, 2))
