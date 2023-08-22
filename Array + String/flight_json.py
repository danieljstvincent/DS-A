import http.client

conn = http.client.HTTPSConnection("flightera-flight-data.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "5133728cc7mshccd7fcfb7538acfp102509jsn255210aa857c",
    'X-RapidAPI-Host': "flightera-flight-data.p.rapidapi.com"
}

conn.request("GET", "/aircraft/search", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))