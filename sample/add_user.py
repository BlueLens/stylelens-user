from __future__ import print_function
from stylelens_user.users import Users
from pprint import pprint
api_instance = Users()

user = {}
user['device_id'] = 'xxxx'

try:
  api_response = api_instance.add_user(user)
  pprint(api_response)
except Exception as e:
  print("Exception when calling add_user: %s\n" % e)
