Here A* algorithm is used to calculate the optimal path from source to the given destination.

f(n) = g(n) + h(n) is the function used in the A* algorithm.

There are 40 locations considered in the map. The picture of the hand drawn map is also submitted. (as Map_Q3_for_reference.jpg)

The edge weights between the different map points are calculated as the duration it takes to move along the edge using the distance metric API of google-maps.

The heuristic function used is the time it takes to reach the destination from each point in the map (again calculated using google's distance metric api)

Execution:

Upon, running the A_star.py file, the user is asked to enter a source and destination from places within the map. The user is then returned the optimal path(giving names of different locations along the way), followed by the the coordinates of the different locations. After that the optimal time to reach the destination from the source is returned. 

After this on the terminal is also a link to a Bing Maps static map showing all the locations and the route. However, this is static.

To get a better view, we can use google_map_path.html file. Just the coordinates array in the script tag of the html file needs to be replaced with the coordinates array printed on the terminal. We can then see the map on the browser (by opening the html file).

Other files:

places.csv - is a list of locations considered in the map.

coordinates - is a list of locations followed by their latitudes and longitudes

Place_to_coordinate.py - Python file to calculate latitude and longitude of the places using the Open_street Map API. Except RGIA and BITS Hyderabad all other points were added using Open_street Map API. These 2 were added separately later as they were not available on Open_street Map API.

edges.csv - has the different edges between the points as shown on the map.

edge_with_weights.csv - has the different edges between nearby points as on the map and the duration it takes to travel between the points as the edge weight.

make_edges_with_weights.py - used to generate edges_with_weights.csv from edges.csv using google's distance metric API.

google_map_path.html - html file which renders the path outputed by the A_star algorithm.




