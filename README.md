# A* Algorithm in Google Maps

Here A* algorithm is used to calculate the **optimal path** from source to the given destination.

## Brief Description
**OpenStreetAPI** is used to fetch the coordinates of townships(localities) in latitude and longitude from the source to the
destination. 
There are **40 locations** considered in the map. The picture of the hand drawn map is also submitted.
The **edge weights** between the different map points are calculated as the duration it takes to move along the edge using the distance metric API of google-maps.
The **heuristic function** used is the time it takes to reach the destination from each point in the map (again calculated using google's distance metric api)

The heuristic function used in the A* algorithm is
> f(n) = g(n) + h(n)


## Installation
- Clone this repository in your preferred directory
 > git clone [https://github.com/Moozzaart23/Astar-algorithm.git]()

 - Run the file to generate the points. 
> python Place_to_coordinate.py

- Run the file to generate edges_with_weights.csv from edges.csv using google’s distance metric API.
>python make_edges_with_weights.py

 - Run the main algorithm file
 >python A_star.py
## Files
The important files in this repository are:
|                		File Name				|Description                                                |
|---------------------------------------|------------------------|
|A_star.py    			| The main file containing the source code
|places.csv          |File containing the list of locations considered in the map.
|coordinates          |The list of locations followed by their latitudes and longitudes
|Place_to_coordinate.py|Python file to calculate latitude and longitude of the places using the Open_street Map API. Except RGIA and BITS Hyderabad all other points were added using Open_street Map API. These 2 were added separately later as they were not available on Open_street Map API.
|edges.csv |This file has the different edges between the points as shown on the map.
|edge_with_weights.csv|This file contains the different edges between nearby points as on the map and the duration it takes to travel between the points as the edge weight.
|make_edges_with_weights.py |Python code used to generate edges_with_weights.csv from edges.csv using google's distance metric API.

## Team Members
- [Anish Dey](https://github.com/Moozzaart23)
- Sanjiv Shenoy
- [Srestha Srivastava](https://github.com/twisted-sres)

