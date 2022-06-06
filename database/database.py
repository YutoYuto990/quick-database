import pymongo
from pymongo import MongoClient
import copy
class DataBase(object):
    def __init__(self):
        self.clint = MongoClient("your mongodb pass")
        self.db = self.clint['test']
    def ping(self):
      return self.clint.admin.command("ping")
    def add_one(self,post:dict):
        return self.db.test.insert_one(post)
    def add_many(self,post:list):
        return self.db.test.insert_many(post)
    def find_and_delete(self,data):
        data=self.get_all(filter=data)
        self.delete(data)
        return data     
    def get(self,filter=None):
      if filter:
        datas=list(self.db.test.find())
        return [i for i in datas if str(filter) in i.keys()]
      else:
        return list(self.db.test.find())
    def up(self,filter,afterdata):
      data=self.get(str(filter))[0]
      self.db.test.update_one(data,{"$set":afterdata})
    def update_one(self,filter,data):
      dat=self.get(str(filter))[0]
      dat[filter]=data
      self.up(filter=filter,afterdata=dat)
    def delete(self,filter):
      data=self.get(str(filter))[0]
      self.db.test.delete_one(data)
    def delete_all(self):
      datas=self.get()
      for data in datas:
        self.db.test.delete_many(data)

    
