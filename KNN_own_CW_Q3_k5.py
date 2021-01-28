# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:33:16 2021

@author: amill
"""


from sklearn import datasets 
iris = datasets.load_iris()
import numpy as np
import statistics as stats

#puesdo code:
# =============================================================================
# step 1) create function that finds distance between two 4-dimenstional vectors 
# step 2) calculate distancce between vector given and each point in x
# step 3) find which value is the smallest distance 
# step 4) check what class the vector which helped create the smallest distance corresponds to 
# =============================================================================
X = iris.data[:, :4]
Target = iris.target


first = np.array([7.2, 3.5, 4.0, 2.4])
second = np.array([7.7, 3.1, 5.8, 1.9])
third = np.array([4.7, 2.8, 4.8, 1.0])
fourth = np.array([6.2, 2.4, 1.4, 0.9])
fifth = np.array([7.7, 3.9, 5.4, 2.0])


def distance(x, y, z, t):
    v = np.sqrt(x**2 + y**2 + z**2 + t**2) 
    return v 

distances = []
for i in range(len(X)):
    a = X[i][0]
    b = X[i][1]
    c = X[i][2]
    d = X[i][3]
    uno = first[0]
    dos = first[1]
    tres = first[2]
    quatro = first[3]    
    x = uno - a
    y = dos - b
    z = tres - c
    t = quatro - d
    distance(x, y, z, t)
    distances.append(distance(x, y, z, t))

ordered = sorted(distances)
smallest_5 = ordered[0:5]

indexes = []
for i in smallest_5:
    for j in distances:
        if i == j:
            indexes.append(distances.index(j))

neighbours_5 = []
for i in indexes:
    add = Target[i]
    neighbours_5.append(add)

print(stats.mode(neighbours_5))

distances = []
for i in range(len(X)):
    a = X[i][0]
    b = X[i][1]
    c = X[i][2]
    d = X[i][3]
    uno = second[0]
    dos = second[1]
    tres = second[2]
    quatro = second[3]    
    x = uno - a
    y = dos - b
    z = tres - c
    t = quatro - d
    distance(x, y, z, t)
    distances.append(distance(x, y, z, t))

ordered = sorted(distances)
smallest_5 = ordered[0:5]

indexes = []
for i in smallest_5:
    for j in distances:
        if i == j:
            indexes.append(distances.index(j))

neighbours_5 = []
for i in indexes:
    add = Target[i]
    neighbours_5.append(add)

print(stats.mode(neighbours_5))

distances = []
for i in range(len(X)):
    a = X[i][0]
    b = X[i][1]
    c = X[i][2]
    d = X[i][3]
    uno = third[0]
    dos = third[1]
    tres = third[2]
    quatro = third[3]    
    x = uno - a
    y = dos - b
    z = tres - c
    t = quatro - d
    distance(x, y, z, t)
    distances.append(distance(x, y, z, t))

ordered = sorted(distances)
smallest_5 = ordered[0:5]

indexes = []
for i in smallest_5:
    for j in distances:
        if i == j:
            indexes.append(distances.index(j))

neighbours_5 = []
for i in indexes:
    add = Target[i]
    neighbours_5.append(add)

print(stats.mode(neighbours_5))

distances = []
for i in range(len(X)):
    a = X[i][0]
    b = X[i][1]
    c = X[i][2]
    d = X[i][3]
    uno = fourth[0]
    dos = fourth[1]
    tres = fourth[2]
    quatro = fourth[3]    
    x = uno - a
    y = dos - b
    z = tres - c
    t = quatro - d
    distance(x, y, z, t)
    distances.append(distance(x, y, z, t))

ordered = sorted(distances)
smallest_5 = ordered[0:5]

indexes = []
for i in smallest_5:
    for j in distances:
        if i == j:
            indexes.append(distances.index(j))

neighbours_5 = []
for i in indexes:
    add = Target[i]
    neighbours_5.append(add)

print(stats.mode(neighbours_5))

distances = []
for i in range(len(X)):
    a = X[i][0]
    b = X[i][1]
    c = X[i][2]
    d = X[i][3]
    uno = fifth[0]
    dos = fifth[1]
    tres = fifth[2]
    quatro = fifth[3]    
    x = uno - a
    y = dos - b
    z = tres - c
    t = quatro - d
    distance(x, y, z, t)
    distances.append(distance(x, y, z, t))

ordered = sorted(distances)
smallest_5 = ordered[0:5]

indexes = []
for i in smallest_5:
    for j in distances:
        if i == j:
            indexes.append(distances.index(j))

neighbours_5 = []
for i in indexes:
    add = Target[i]
    neighbours_5.append(add)

print(stats.mode(neighbours_5))