# written by Taylor Graham
# taylor.s.graham@colorado.edu
# Student ID: 100512193

# On my honor, as a University of Colorado at Boulder student,
# I have neither given nor received unauthorized assistance on this work

import sys, csv, numpy
import matplotlib.pyplot as plt
import datetime as dt

def read_csv_file(filename):
#	csv data format	expected:
#	"date","close","volume","open","high","low"
	data=[]
	with open(filename) as f:
		next(f)
		next(f)
		csvreader = csv.reader(f)
		for row in csvreader:
			data.append(row)

	return data

def process_single_attribute(data, attribute_num, normalization_type):
	array=[]
	normalized_array=[]
	for line in data:
		array.append(float(line[attribute_num]))
	if (normalization_type == 'min-max'):
		minimum=min(array)
		maximum=max(array)
		# apply min-max normalization
		for num in array:
			normalized_array.append((num-minimum)/(maximum-minimum))
	if (normalization_type == 'z-score'):
		mean = numpy.mean(array)
		std = numpy.std(array)
		# apply z-score normalization
		for num in array:
			normalized_array.append((num-mean)/std)

	for i in range(len(array)):
		print "{0}\t{1}".format(array[i],normalized_array[i])

def process_two_attributes(data1,data2):
	high1,low1,close1,high2,low2,close2=[],[],[],[],[],[]
	for line in data1:
		high1.append(line[4])
		low1.append(line[5])
		close1.append(line[1])
	for line in data2:
		high2.append(line[4])
		low2.append(line[5])
		close2.append(line[1])
	val = [numpy.corrcoef(high1,low1)[0][1]]
	val.append(numpy.corrcoef(high2,low2)[0][1])
	val.append(numpy.corrcoef(close1,close2)[0][1])
	print "{0}\t{1}\t{2}".format(val[0],val[1],val[2])

def home_depot_analysis():
	data = read_csv_file('hd_3yrs.csv')
	date,close,volume,openv,high,low=[],[],[],[],[],[]
	for line in data:
		year,mon,day = line[0].split('/')
		date.append(dt.date(int(year),int(mon),int(day)))
		close.append(float(line[1]))
		volume.append(float(line[2]))
		openv.append(float(line[3]))
		high.append(line[4])
		low.append(line[5])

	fig = plt.figure(1)
	plt.title('Change in High and Low attributes of HD Stock')
	line_high,=plt.plot_date(date,high, linestyle='-', color='b', ms=.1) 
	line_low,=plt.plot_date(date,low, linestyle='-', color='r', ms=.1)
	plt.legend([line_high, line_low], ['High', 'Low'])
	fig.autofmt_xdate()
	plt.xlabel('Date')
	plt.ylabel('Value of stock ($)')
	plt.grid(True)
	
	fig=plt.figure(2)
	plt.title('Boxplot of the Open and Close values of HD Stock')
	plt.boxplot([openv,close])
	plt.ylabel("Value of stock")
	plt.xticks([1,2], ["Opening Price", "Closing Price"])
	plt.grid(True)
	
	fig=plt.figure(3)
	plt.title('Histogram of the Trade Volume of HD Stock')
	plt.hist(volume, facecolor='g', alpha=0.75)
	plt.xlabel('Volume of Stock')
	plt.ylabel('Probability')
	plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,8))
	plt.grid(True)

	fig=plt.figure(4)
	plt.title('Trade Volume of HD Stock by date')
	plt.bar(date, volume, color='blue')
	fig.autofmt_xdate()
	plt.ylabel('Number of stock trades')
	plt.xlabel('Date')
	plt.ticklabel_format(axis='y', style='sci', scilimits=(-1,8))

	plt.show()

	max_vol = max(volume)
	for i in range(len(volume)):
		if volume[i] == max_vol:
			index=i
	print date[index] # 2012-5-15
	# fun fact ^ may 15th is the day that HD releases its Q4 sales figures each year	

def usage():
	print 'TODO'
	sys.exit(0)

def main():
	if (len(sys.argv) != 3):
		usage()
	data1 = read_csv_file(sys.argv[1])
	data2 = read_csv_file(sys.argv[2])
	print "Normalizing the Volume attribute of file {}".format(sys.argv[1])
	process_single_attribute(data1, 2, 'min-max')
	print
	print "Normalizing the Open attribute of the file {}".format(sys.argv[2])
	process_single_attribute(data2, 3, 'z-score')
	print
	print "Processing the correlation coefficients for the following values:"
	print """{0} High and Low attribute, {1} High and Low attribute,
	\rAnd the Close attribute between {0} and {1}""".format(sys.argv[1],sys.argv[2])
	process_two_attributes(data1,data2)

	home_depot_analysis()

if __name__ == "__main__":
	main()