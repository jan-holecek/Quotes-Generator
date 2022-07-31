import http.client
import json    

conn = http.client.HTTPSConnection("quotes15.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "quotes15.p.rapidapi.com",
    'x-rapidapi-key': "KEY"
}

conn.request("GET", "/quotes/random/?language_code=cs", headers=headers)

res = conn.getresponse()
data = res.read().decode("utf-8")
parse_json = json.loads(data)
content = '"' + parse_json["content"] + '"'

