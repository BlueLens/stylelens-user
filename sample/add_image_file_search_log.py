from __future__ import print_function
from stylelens_user.user_logs import UserLogs
from pprint import pprint
api_instance = UserLogs()

device_id = 'xxxx'
log = {}
log['aaa'] = 'aaa'

try:
  api_response = api_instance.add_image_file_search_log(device_id, log)
  pprint(api_response)
except Exception as e:
  print("Exception when calling add_image_file_search_log: %s\n" % e)
