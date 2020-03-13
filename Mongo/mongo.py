import pymongo as pm


class PharmaDBMainDS:
    def __init__(self):
        self.MC = None
        self.coll = None

    def server_connect(self, link):
        try:
            self.MC = pm.MongoClient(link)
            self.coll = self.MC.PharmaDB.mainDS
        except:
            raise RuntimeError

    def set_localhost(self):
        self.server_connect('mongodb://localhost:27017/')

    def set_live_host(self, link):
        self.server_connect(link)

    def find(self, qy, need={}):
        if not need:
            need = {}
        return list(self.coll.find(qy, need))
