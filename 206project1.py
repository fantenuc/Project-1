import os
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.

	#Your code here:
	read_file = open(file, 'r')
	lst = []
	for line in read_file.readlines()[1:]:
		dic = {}
		line = line.split(',')
		dic['First'] = line[0]
		dic['Last'] = line[1]
		dic['Email'] = line[2]
		dic['Class'] = line[3]
		dic['DOB'] = line[4].strip()
		lst.append(dic)
	#print(lst)
	return lst


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	sorted_data = sorted(data, key = lambda x: x[col])
	return sorted_data[0]['First'] + ' ' + sorted_data[0]['Last']


#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	fresh = 0
	soph = 0
	jun = 0
	senior = 0
	for dic in data:
		if dic['Class'] == 'Freshman':
			fresh += 1
		if dic['Class'] == 'Sophomore':
			soph += 1
		if dic['Class'] == 'Junior':
			jun += 1
		if dic['Class'] == 'Senior':
			senior += 1
	lst = []
	fresh_tuple = ('Freshman', fresh)
	lst.append(fresh_tuple)
	soph_tuple = ('Sophomore', soph)
	lst.append(soph_tuple)
	jun_tuple = ('Junior', jun)
	lst.append(jun_tuple)
	senior_tuple = ('Senior', senior)
	lst.append(senior_tuple)

	sorted_lst = sorted(lst, key = lambda x: x[1], reverse = True)
	return sorted_lst




# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	day_count = {}
	for day in a:
		birthday = day['DOB']
		day = birthday.split('/')
		num = day[1]
		if num not in day_count:
			day_count[num] = 1
		else:
			day_count[num] += 1
	day_lst = []
	for key in day_count.keys():
		day_tup = (key, day_count[key])
		day_lst.append(day_tup)
	sorted_lst = sorted(day_lst, key = lambda x: x[1], reverse = True)
	return int(sorted_lst[0][0])


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	year = []
	ages = []
	count = 0
	for date in a:
		birthday = date['DOB']
		year_born = birthday[-4:]
		years = int(year_born)
		year.append(years)
	for date in year:
		age = 2017 - date
		ages.append(age)
	for elem in ages:
		count += elem
	average_age = count // len(ages)
	return average_age



#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	sorted_data = sorted(a, key = lambda x: x[col])
	#print(sorted_data)
	csv_file = open(fileName, 'w')
	for data in sorted_data:
		csv_file.write('{},{},{}\n'.format(data['First'], data['Last'], data['Email']))
	csv_file.close()




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
