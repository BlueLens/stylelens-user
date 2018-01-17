from __future__ import print_function
from stylelens_user.users import Users
from pprint import pprint
api_instance = Users()

device_id = "xxxx"

try:
  api_response = api_instance.get_user_by_device_id(device_id)
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_user_by_device_id: %s\n" % e)
