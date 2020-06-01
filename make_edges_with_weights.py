import urllib.request
import json

def dist(src_lat, src_lng, dest_lat, dest_lng):
    endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&'
    api_key = 'Enter Your Key here'
    nav_request = 'origins={}&destinations={}&key={}'.format(src_lat+','+src_lng,dest_lat+','+dest_lng,api_key)
    request = endpoint + nav_request
    response = urllib.request.urlopen(request).read()
    duration = json.loads(response)
    duration = duration['rows'][0]['elements'][0]['duration']['value']
    duration = float(duration/60)
    return duration


#Dictionary 1 : NOP -> (latitude,longitude)

import pandas
df = pandas.read_csv('coordinates.csv')

df2 = pandas.read_csv('places.csv')

NOP_coordinate = {}

cnt=0;
for i in df2['Locations']:
    NOP_coordinate[i] = (float(df['Latitude'][cnt]),float(df['Longitude'][cnt]))
    cnt+=1


#Dictionary 2 : NOP -> [list of (NOP,edge_weight) to which it goes]

df3 = pandas.read_csv('edges.csv')
df3['weight'] = df3['Source']

for i in range(68):
    s1 = df3['Source'][i]
    s2 = df3['Destination'][i]
    df3['weight'][i] = dist(str(NOP_coordinate[s1][0]),str(NOP_coordinate[s1][1]),str(NOP_coordinate[s2][0]),str(NOP_coordinate[s2][1]))
    

import csv

with open('edge_with_weights.csv','w',newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Source','Destination','Weight'])
    for i in range(68):
        thewriter.writerow([df3['Source'][i], df3['Destination'][i], df3['weight'][i]])


