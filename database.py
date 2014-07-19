import pickle

dbFile = 'YTpU.db'

def LoadDB():
    result = {}
    try:
        with open(dbFile, 'rb') as f:
             result = pickle.load(f)
    except Exception:
        SaveDB({'jovemnerd':[]})
    finally:
        return result

def SaveDB(db):
    with open(dbFile, 'wb') as f:
        pickle.dump(db, f)
