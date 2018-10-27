#!/usr/bin/env python

import argparse
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import string

description=""

parser = argparse.ArgumentParser( description=description )
parser.add_argument(
	"data_file",
	help="path to the input data file",
)
parser.add_argument(
	"--x_value",
	required=True,
	type=int,
	help="1-based index of the column for x values",
)
parser.add_argument(
        "--y_value",
        type=int,
	required=True,
        help="1-based index of the column for y values",
)
parser.add_argument(
        "--strat",
        type=int,
        default=-1,
        help="1-based index of the column for categorical series values",
)
parser.add_argument(
        "--output_file",
	required=False,
	default="./output.png",
        help="path to the output data file",
)
args = parser.parse_args( )

def load_data(path, x, y, z):
	answer = []
	fh = open(path)
	
	heading = fh.readline()
	heading = heading.split("\t")
	axis = [heading[x-1]]
	axis.append(heading[y-1])

	axis[0] = ''.join(ch for ch in axis[0] if ch.isalpha() or ch.isspace() or ch == '(' or ch == ')')
	axis[1] = ''.join(ch for ch in axis[1] if ch.isalpha() or ch.isspace() or ch == '(' or ch == ')')

	lines = fh.readlines()[1:]

	x_val = []
	y_val = []
	z_val = []
	
	for line in lines:
		data = line.split("\t")
		x_val.append(float(data[x-1]))
		y_val.append(float(data[y-1]))
		if z != -1:
			z_val.append(data[z-1].rstrip('\n'))

	#print(x_val)
	#print(y_val)		
	#print(axis)
	#print(z_val)

	fh.close()
	
	return axis, x_val, y_val, z_val

def transform_data(x, y, z):
	
	z_unique = list(set(z))
	#print(z_unique)

	idx = []
	data = []
	zvals = []

	for i in range(len(z_unique)):
		idx.append([index for index, value in enumerate(z) if value == z_unique[i]])

	for i in range(len(idx)):
		data.append(([float(x[j]) for j in idx[i]], [float(y[j]) for j in idx[i]]))
		zvals.append([z[j] for j in idx[i]])
	
	#print(zvals)

	return data, zvals, z_unique

def plot_graph(axis, data, z, categorical, output):

	#colors = ['blue', 'orange', 'green']
	#data = (x, y, z)
	groups = categorical

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)

	if not groups:
		colors = ['blue']
		x, y = data
		ax.scatter(x, y, c=colors)
		
	else:
		for data, group in zip(data, groups):
			x, y = data	
			ax.scatter(x, y, label=group)
			plt.legend(loc='best')

	plt.xlabel(axis[0])
	plt.ylabel(axis[1])
	#plt.show()
	plt.savefig(output)
		

axis, xvals, yvals, zvals = load_data(args.data_file, 
					args.x_value, 
					args.y_value,
					args.strat)

groups = []

if zvals:
	data, zvals, groups = transform_data(xvals, yvals, zvals)
else:
	data = [xvals, yvals]
	#print(data)
	zvals = []

plot_graph(axis, data, zvals, groups, args.output_file)
