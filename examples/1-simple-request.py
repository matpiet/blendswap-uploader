# Tested in Python 3.4
# Tested in Blender 2.69
# This should work on Blender 2.5 and up

import json
from http.client import HTTPConnection as Connection

header = {'Accept': 'application/json,text/javascript,*/*; q=0.01'}

# Create the connection and request it
conn = Connection("dev.blendswap.com", 80)
try:
	conn.request("GET", "/blends/index/page:1.json", headers=header)
except:
	raise

# Display results
res = conn.getresponse()
# the response contains bytes
# We have to parse it
body = res.read().decode("utf-8")

# Print the entire result
print("\n\nFULL RETURNED BODY *********************")
print(json.loads(body))
# Print just the author of the first blend
print("\n\nTHE BLEND AUTHOR ***********************")
print(json.loads(body)['data'][0]['User'])
