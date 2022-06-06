import database
import copy
class NoSuchData(Exception):
    pass
class DataAlreadyExists(Exception):
    pass
class Client:
    def __init__(self):
        self.db=database.DataBase()
    def get_user(self,id):
        data=self.db.get(str(id))
        if data:
          if data[0][str(id)]["type"]=="user":
            return data[0]
        else:
            raise NoSuchData("no such user")
    def get_all_user(self):
        da=self.db.get()
        ids=[list(i.keys())[-1] for i in da]
        return [d for d,id in zip(da,ids) if d[id]["type"]=="user"]
    def get_users_attr(self,id,attr):
      try:
        data=self.get_user(id)
        return data[id][attr]
      except Exception as e:
        return e
    def add_user(self,id):
        dat=self.db.get(str(id))
        if dat:
            raise DataAlreadyExists("user alredy exists")
        else:
            self.db.add_one({str(id):{"type":"user"}})
    def update_user(self,id,attr,data):
      try:
        member=self.db.get(str(id))[0]
        datas=copy.deepcopy(member)
        member[str(id)][attr]=data
        self.db.db.test.update_one(datas,{"$set":member})
      except:
            raise NoSuchData("no such user")
    def delete_user(self,id):
      try:
        self.db.delete(str(id))
      except:
        raise NoSuchData("no such user")
    def add_guild(self,id):
        guild=self.db.get(str(id))
        if guild:
            raise DataAlreadyExists("guild alredy exists")
        else:
            self.db.add_one({str(id):{"type":"guild"}})
    def get_guild(self,id):
        data=self.db.get(str(id))
        if data:
          if data[0][str(id)]["type"]=="guild":
            return data[0]
        else:
            raise NoSuchData("no such guild")
    def get_all_guild(self):
        da=self.db.get()
        ids=[list(i.keys())[-1] for i in da]
        return [d for d,id in zip(da,ids) if d[id]["type"]=="guild"]
    def get_guild_attr(self,id,attr):
      try:
        data=self.get_guild(id)
        return data[id][attr]
      except Exception as e:
        return e
    def update_guild(self,id,attr,data):
      try:
        member=self.db.get(str(id))[0]
        datas=copy.deepcopy(member)
        member[str(id)][attr]=data
        self.db.db.test.update_one(datas,{"$set":member})
      except:
          raise NoSuchData("no such guild")
    def delete_guild(self,id):
        self.db.delete(str(id))