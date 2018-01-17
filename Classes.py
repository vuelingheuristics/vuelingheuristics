import read_file.py

#class for planes
class Plane(object):

FUEL_START = 3199
SPEED_PLANE = 800
SEATS_IN_PLANE = 199
BOARDING_TIME = 1
UNBOARDING_TIME = 1
REFUEL_TIME = 1

    def __init__(self):
        self.plane_list = []

    def speed(self):

    def fuel(self):

    def seats(self):

    def refueling(self):

    def boarding(self):

    def un_boarding(self):

#class for destinations
class Location(object):
    def __init__(self):
        self.location_list = []

        #function for retrievinf distance between two cities
    ''''def get_distance(city1, city2):
        start = list_destinations.[city1]? #getting both cities form the list
        end = list_destinations.[city2]

        distance = list_distances[row,column] #row as start and column as end position



    get_distance('Amsterdam', 'Moscow')'''

#class for passengers
class Passenger(object):
    def __init__(self):
        self.passenger_list = []

#constraint boarding time

#constraint fuel

#constraint detour

#constraint flight time
