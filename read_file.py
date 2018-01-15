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
        return (loc_a, cor_x, cor_y, loc_z)

def reading_data_distances():
    matrix = np.loadtxt('MokumAirwaysDistances.txt')
    print (matrix)

def reading_data_transport():
    matrix = np.loadtxt('MokumAirwaysPassengers.txt')
    print (matrix)

def plot_data():
    reading_data_locations()
    plt.scatter(cor_x, cor_y, label='Map of destinations')
    plt.xlabel('coordinate x')
    plt.ylabel('coordinate y')
    for i, txt in enumerate(loc_z):
        plt.annotate(txt, (cor_x[i],cor_y[i]))
    plt.show()

reading_data_transport()
