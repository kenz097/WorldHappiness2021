import pymongo


# define connection pool
def connection_pool():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    col = client["WorldHappiness2021"]["WorldHappiness2021"]
    return col
