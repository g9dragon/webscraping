import pymongo

def savefile(ct):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["ScrapedData"]

    mylist = ct

    x = mycol.insert_many(mylist)
    
