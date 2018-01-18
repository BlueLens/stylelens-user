from __future__ import print_function
from stylelens_user.users import Users
from pprint import pprint
api_instance = Users()

device_id = 'xxxx'
image = {}
image['xxxxx'] = 'xxxx'

try:
  api_response = api_instance.add_image(device_id, image)
  pprint(api_response)
except Exception as e:
  print("Exception when calling add_object: %s\n" % e)
