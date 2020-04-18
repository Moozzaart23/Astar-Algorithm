import pandas
df = pandas.read_csv('places.csv')


import geopy
from geopy.geocoders import Nominatim
nom = Nominatim(user_agent="my-application")



df['Locations'] = df['Locations'] + ' , Hyderabad, Telangana, India'
df['Latitude'] = df['Locations']
df['Longitude'] = df['Locations']


for i in range(len(df['Locations'])):
    n = nom.geocode(df['Locations'][i])
    df['Latitude'][i] = n.latitude if n != None else None 
    df['Longitude'][i] = n.longitude if n != None else None


import csv

print(df)

# Uncomment below code to add to create the coordinates.csv file
# However, BITS Hyderabad and RGIA must be added later manually.

'''

with open('coordinates.csv','w',newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Locations','Latitude','Longitude'])
    for i in range(42):
        thewriter.writerow([df['Locations'][i], df['Latitude'][i], df['Longitude'][i]])


 '''
    




