import pickle

dbFile = 'YTpU.db'

def loadDB():
    result = {}
    try:
        with open(dbFile, 'rb') as f:
             result = pickle.load(f)
    except Exception:
        saveDB({})
    finally:
        return result

def saveDB(db):
    with open(dbFile, 'wb') as f:
        pickle.dump(db, f)

if __name__ == '__main__':
    db = loadDB()    
