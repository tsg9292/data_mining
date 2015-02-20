# written by Taylor Graham
# taylor.s.graham@colorado.edu
# Student ID: 100512193

# On my honor, as a University of Colorado at Boulder student,
# I have neither given nor received unauthorized assistance on this work

import sys
import itertools

def set_up_data():
	t1=['e','g','s','f','z']
	t2=['b','e','d','i','n']
	t3=['b','e','i','n','o']
	t4=['b','g','i','n','z']
	t5=['b','g','n','t','z']
	data=[t1,t2,t3,t4,t5]
	return data

def supp(item, data):
	count=0
	tmpcount=0
	for trial in data:
		for letter in item:
			if letter in trial:
				tmpcount=tmpcount+1
		if tmpcount == len(item):
			count=count+1
		tmpcount=0
	return count

def add_frequent_combinations(letters, num, data):
	frequent_sets=[]
	new_combinations=list(itertools.combinations(letters, num))
	for item in new_combinations:
		if (supp(item,data) >= 0):
			frequent_sets.append(item)
	return frequent_sets

def main():
	data=set_up_data()
	letters=['b','d','e','f','g','i','n','o','s','t','z']
	frequent_letters=[]
	for letter in letters:
		if (supp(letter, data) > 2):
			frequent_letters.append(letter)
	frequent_sets=list(frequent_letters)

	#frequent_sets=frequent_sets+add_frequent_combinations(frequent_letters, 2, data)
	#frequent_sets=frequent_sets+add_frequent_combinations(frequent_letters, 3, data)
	frequent_sets=frequent_sets+add_frequent_combinations(frequent_letters, 4, data)
	#frequent_sets=frequent_sets+add_frequent_combinations(frequent_letters, 5, data)

	print frequent_sets

if __name__ == "__main__":
	main()