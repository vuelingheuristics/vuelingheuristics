#reading file for setting up data
import matplotlib.pyplot as plt
import csv
import numpy as np

loc_a = []
cor_x = []
cor_y = []
loc_z = []


def reading_data_locations():
    with open('MokumAirwaysCities.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            loc_a.append(int(row[0]))
            cor_x.append(int(row[1]))
            cor_y.append(int(row[2]))
            loc_z.append(str(row[3]))
        print (loc_a, cor_x, cor_y, loc_z)

def reading_data_distances():
    with open('MokumAirwaysDistances.txt', 'r') as list_distances:
        for lines in list_distances:
            line = lines.splitlines()
            matrix = np.array(line)
            print(matrix)

def reading_data_transport():
    with open('MokumAirwaysPassengers.txt', 'r') as list_passengers:
        for lines in list_passengers:
            line = lines.splitlines()
            matrix = np.array(line)
            print(matrix)

def plot_data():
    reading_data_locations()
    plt.scatter(cor_x, cor_y, label='Map of destinations')
    plt.axis([min(cor_x), max(cor_x), max(cor_y), 0])
    plt.xlabel('coordinate x')
    plt.ylabel('coordinate y')
    for i, txt in enumerate(loc_z):
        plt.annotate(txt, (cor_x[i],cor_y[i]))
    plt.show()

reading_data_distances()
