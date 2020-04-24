import urllib.request
import json

def dist(src_lat, src_lng, dest_lat, dest_lng):
    endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&'
    api_key = 'AIzaSyAMWJctuV0azNvNCm6zS9ASEZj_xn-dbIM'
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

df3 = pandas.read_csv('edge_with_weights.csv')


Edges = {}

for i in range(41):
    Edges[df2['Locations'][i]] = []

for i in range(68):
    Edges[df3['Source'][i]].append((df3['Destination'][i],df3['Weight'][i]))
    Edges[df3['Destination'][i]].append((df3['Source'][i],df3['Weight'][i]))
    

#Implement A*
start = input("Enter Source: ")
end = input("Enter Destination: ")

#Dictionary 3 : NOP -> Heuristic Value

Heuristic = {}
    
df4 = pandas.read_csv('places.csv')

for i in range(41):
    s1 = df4['Locations'][i]
    s2 = end
    Heuristic[s1] = dist(str(NOP_coordinate[s1][0]),str(NOP_coordinate[s1][1]),str(NOP_coordinate[s2][0]),str(NOP_coordinate[s2][1]))

open_list = [(0+Heuristic[start],start)]

parent = {}

f_n = {} #f(n) value for the nth node.

for i in df2['Locations']:
    f_n[i] = 1000000000

mx = 1000000000
closed=[]
f_n[start] = Heuristic[start]

# end when open_list is empty or when we have reached goal and there is 
# no shorter path.
while( (len(open_list) > 0) and (mx > open_list[0][0])):
    next_closest = open_list[0]
    del(open_list[0])
    closed.append(next_closest[1])
    
    if(next_closest[1] == end):
        mx = next_closest[0]
    
    for i in Edges[next_closest[1]]:
        f = next_closest[0] - Heuristic[next_closest[1]] + Heuristic[i[0]] + i[1]
        if f < f_n[i[0]]:
            t = (f_n[i[0]],i[0])
            parent[i[0]] = next_closest[1]
            if (t in open_list):
                open_list.remove(t)
                open_list.append((f,i[0]))
                f_n[i[0]] = f
            elif i[0] in closed:
                closed.remove(i[0])
                open_list.append((f,i[0]))
                f_n[i[0]] = f
            else:
                open_list.append((f,i[0]))
                f_n[i[0]] = f

node = end
path = []
coordinates = []

while(node != start):
    path.append(node)
    node = parent[node]
    
path.append(start)

path.reverse()

for node in path:
    c = []
    c.append(NOP_coordinate[node][0])
    c.append(NOP_coordinate[node][1])
    coordinates.append(c)

print("Path is ")
print(path)
print()
print("Coordinates of the points are ")
print(coordinates)
print()
print("Optimal duration of the journey is")
print(f_n[end])
print('\n')

url = "https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?"
for i in range(len(coordinates)):
    url = url + "wp."+str(i)+"="+str(coordinates[i][0])+","+str(coordinates[i][1])+"&"
url = url + "key=AlHaFbrw006PkrgcKFwhW_fO8mpDq5w8gZc47tAfnRfVZj1gmTg6fq3y0n9m-ZIB"

print("Bing Map Url is :\n")
print(url)
print('\n')
print("To see a better view on google map, just copy-paste the coordinates from the terminal to",end=" ")
print("the google_map_path.html file and see the html file on the browser !")

print('\n')
