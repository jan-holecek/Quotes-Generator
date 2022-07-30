import http.client
import json    

conn = http.client.HTTPSConnection("quotes15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "quotes15.p.rapidapi.com",
    'x-rapidapi-key': "b18e61a8f8mshfed36e7f4426c8fp1ff287jsnc71baf639749"
}

conn.request("GET", "/quotes/random/?language_code=cs", headers=headers)

res = conn.getresponse()
data = res.read().decode("utf-8")
parse_json = json.loads(data)
content = '"' + parse_json["content"] + '"'

