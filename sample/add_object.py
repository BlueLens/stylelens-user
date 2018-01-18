from __future__ import print_function
from stylelens_user.users import Users
from pprint import pprint
api_instance = Users()

image_id = ""
object = {}
object ['xxxxx'] = 'xxxx'

try:
  api_response = api_instance.add_object(object)
  pprint(api_response)
except Exception as e:
  print("Exception when calling add_object: %s\n" % e)
