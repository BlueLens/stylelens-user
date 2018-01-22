from __future__ import print_function
from stylelens_user.users import Users
from pprint import pprint
api_instance = Users()

device_id = 'xxxx'

try:
  api_response = api_instance.increase_user_profile_price(device_id, 'low_mid')
  pprint(api_response)
except Exception as e:
  print("Exception when calling increase_user_profile_price: %s\n" % e)
