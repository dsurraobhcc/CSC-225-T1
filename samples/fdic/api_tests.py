'''
Testing the API https://banks.data.fdic.gov/docs/

According to the docs, you will need an API key in the future:
https://api.data.gov/signup/

Using curl from the command line:
curl -X GET "https://banks.data.fdic.gov/api/institutions?filters=STALP%3AIA%20AND%20ACTIVE%3A1&fields=ZIP%2COFFDOM%2CCITY%2CCOUNTY%2CSTNAME%2CSTALP%2CNAME%2CACTIVE%2CCERT%2CCBSA%2CASSET%2CNETINC%2CDEP%2CDEPDOM%2CROE%2CROA%2CDATEUPDT%2COFFICES&sort_by=OFFICES&sort_order=DESC&limit=10&offset=0&format=json&download=false&filename=data_file" -H "accept: application/json"

HOWTO Fetch Internet Resources Using The urllib Package
https://docs.python.org/3/howto/urllib2.html?highlight=urllib

JSON
https://docs.python.org/3/library/json.html#module-json
'''
import urllib.request
import json

# Financial institution demographic and location information
# url = 'https://banks.data.fdic.gov/api/institutions'
url = 'https://banks.data.fdic.gov/api/institutions?filters=STALP%3AIA%20AND%20ACTIVE%3A1&fields=ZIP%2COFFDOM%2CCITY%2CCOUNTY%2CSTNAME%2CSTALP%2CNAME%2CACTIVE%2CCERT%2CCBSA%2CASSET%2CNETINC%2CDEP%2CDEPDOM%2CROE%2CROA%2CDATEUPDT%2COFFICES&sort_by=OFFICES&sort_order=DESC&limit=10&offset=0&format=json&download=false'
with urllib.request.urlopen(url) as response:
   data = response.read()
   json_data = json.loads(data)
   # print(json_data['data'])
   for row in json_data['data']:
       row_data = row['data']
       print(row_data['NAME'], row_data['CITY'], row_data['COUNTY'], \
           row_data['ZIP'])