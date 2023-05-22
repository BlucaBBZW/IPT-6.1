from pymongo import MongoClient

connectionString = "mongodb+srv://lucibluc:luci69@cluster0.rtex13l.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connectionString)
db = client["Newslater"]
col = db["emails"]


class Db:
    def getSubs():
        Subs = col.find({})

        SubsList = []
        for e in Subs:
            SubsList.append(e['Email'])
        return SubsList