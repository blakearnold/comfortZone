import User
import Place
import RecommendationEngine
import Getter
import pymongo
from pymongo import Connection
connection = Connection()
connection = Connection('localhost', 27017)
db = connection['test-database']
coll=db['checkin']
allGet=Getter.AllGet(coll)
allGet.pullUs()

r = RecommendationEngine.RecommendationEngine()
#TODO:
user1 = set([])
r.runRec(2, 2, allGet.pullPl())


