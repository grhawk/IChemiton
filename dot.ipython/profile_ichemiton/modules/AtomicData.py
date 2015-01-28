
import os

atomic_numb = []
atomic_name = []
atomic_mass = []
atomic_symb = []
for line in open('/home/petragli/MyProjects/IChemiton/profile_ichemiton/config/pt-data1.csv', 'r'):
    fields = line.split(',')
    atomic_mass.append(fields[3])
    atomic_name.append(fields[2])
    atomic_symb.append(fields[1])
    atomic_numb.append(fields[0])


def findAtNumb(atnumb):
    index = atnumb - 1
    return ([atomic_name[index], atomic_mass[index], atomic_symb[index]])
