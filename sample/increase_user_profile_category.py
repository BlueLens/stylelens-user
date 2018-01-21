from __future__ import print_function
from stylelens_user.users import Users
from pprint import pprint
api_instance = Users()

device_id = 'xxxx'

try:
  api_response = api_instance.increase_user_profile_category(device_id, 'blouse')
  pprint(api_response)
except Exception as e:
  print("Exception when calling increase_user_profile_category: %s\n" % e)
