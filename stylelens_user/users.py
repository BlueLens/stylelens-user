from bson.objectid import ObjectId
from stylelens_user.database_user import DataBaseUser

class Users(DataBaseUser):
  def __init__(self):
    super(Users, self).__init__()
    self.users = self.db.users

  def add_user(self, user):
    query = {}

    query['device_id'] = user['d_id']

    try:
      r = self.users.update_one(query,
                                {"$set": user},
                                upsert=True)
    except Exception as e:
      print(e)

    if 'upserted' in r.raw_result:
      id = str(r.raw_result['upserted'])
      return id
    else:
      return None

  def get_user_by_id(self, id):
    query = {}
    query['_id'] = ObjectId(id)
    try:
      r = self.users.find_one(query)
    except Exception as e:
      print(e)

    return r

  def get_user_by_device_id(self, id):
    query = {}
    query['device_id'] = id
    try:
      r = self.users.find_one(query)
    except Exception as e:
      print(e)

    return r
