#!/usr/bin/env python

# written by Taylor Graham
# taylor.s.graham@colorado.edu
# Student ID: 100512193

# On my honor, as a University of Colorado at Boulder student,
# I have neither given nor received unauthorized assistance on this work

import getopt, sys, numpy
import matplotlib.pyplot as plt

def process_ith_attribute(i):
	N=len(i)
	minimum=min(i)
	maximum=max(i)
	mean=numpy.mean(i)
	std=numpy.std(i)
	return (N,minimum,maximum,mean,std)

def process_jth_attribute(j):
	Q1=numpy.percentile(j, 25)
	median=numpy.percentile(j, 50)
	Q3=numpy.percentile(j, 75)
	IQR=Q3-Q1
	return (Q1, median, Q3, IQR)

def gather_data():
	data=[[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
	with open("housing.data.txt") as f:
		for line in f:
			(crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat,medv) = line.split()
			data[0].append(float(crim))
			data[1].append(float(zn))
			data[2].append(float(indus))
			data[3].append(int(chas))
			data[4].append(float(nox))
			data[5].append(float(rm))
			data[6].append(float(age))
			data[7].append(float(dis))
			data[8].append(int(rad))
			data[9].append(float(tax))
			data[10].append(float(ptratio))
			data[11].append(float(b))
			data[12].append(float(lstat))
			data[13].append(float(medv))

	return data

def print_results(i,j,N,minimum,maximum,mean,std,Q1,median,Q3,IQR):
	names=['crim','zn','indus','chas','nox','rm','age','dis','rad','tax','ptratio','b','lstat','medv']
	print "Stats for data set number {0:d}: {1}".format(i,names[i])
	print "Number of objects: {0:d}".format(N)
	print "Min: {0:.3f}".format(minimum)
	print "Max: {0:.3f}".format(maximum)
	print "Mean: {0:.3f}".format(mean)
	print "Standard Deviation: {0:.3f}".format(std)
	print
	print "Stats for data set number {0:d}: {1}".format(j,names[j])
	print "Q1: {0:.3f}".format(Q1)
	print "median: {0:.3f}".format(median)
	print "Q3: {0:.3f}".format(Q3)
	print "IQR: {0:.3f}".format(IQR)

def usage():
	print 'TODO'
	sys.exit(0)

def main():
	if (len(sys.argv) != 3):
		usage()
	i=int(sys.argv[1])
	j=int(sys.argv[2])
	#TODO add checks to make sure i,j E[0,13]
	data=gather_data()
	(N,minimum,maximum,mean,std)=process_ith_attribute(data[i])
	(Q1,median,Q3,IQR)=process_jth_attribute(data[j])
	print_results(i,j,N,minimum,maximum,mean,std,Q1,median,Q3,IQR)
	plt.scatter(data[i],data[j])
	plt.show()

if __name__ == "__main__":
	main()