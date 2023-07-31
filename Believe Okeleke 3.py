# Question 1 - write a code to find the second largest number in a list of integers after sorting the list:

numbers = [10,5,20,15,8]
sortedList = sorted(numbers)
# Find the index of the second largest number
secondLargestNumberIndex = len(sortedList) - 2
print('Second Largest Number is:', sortedList[secondLargestNumberIndex])

#Queston 2 - Write a code to find the common elements between two lists of integers:

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
commonElements = []

for num in list1:
    for value in list2:
        if num == value:
            commonElements.append(num)

result = ""
for value in commonElements:
    result += str(value) + ', '

print('Common Elements: ', result.rstrip(', '))



#Question 3 - write a code to create a new list with only the even numbers from the original list:

numbers2 = [1,2,3,4,5,6,7,8]
evenNumbers = []

for num in numbers2:
    if num % 2 == 0:
        evenNumbers.append(num)

print("List of even numbers: ", evenNumbers)


#Question 4 - Create a tuple of even numbers and write Python code to reverse its elements

evenTuple = (2,4,6,8,10,12,14,16,18,20)
# Convert tuple to list
evenList = list(evenTuple)
#Reverse list 
evenListRvrs = evenList[::-1]
#Convert the reversed list to tuple
evenTupleRvrs = tuple(evenListRvrs)
print('Reversed Tuple:', evenTupleRvrs)




#Question 5 - Create a tuple of even integers including duplicates and write Python code to create a new tuple with only the unique elements, removing duplicates

myTuple = (2,2,8,8,4,22,10,10,32,12,102,44,92,102)
# convert tuple to list
myList = list(myTuple)
sortedMyList = sorted(myList)

noDuplicatesList = []

for num in sortedMyList:
    if num in noDuplicatesList:
        continue
    else:
        noDuplicatesList.append(num)

noDuplicatesTuple = tuple(noDuplicatesList)
print("No Even Duplicates: ", noDuplicatesTuple)


#Question 6 - Create a tuple of odd integers including duplicates and write Python code to create a new tuple with only the unique elements, removing duplicates

oddNum = (3,3,7,7,5,23,11,11,33,13,103,45,93,103)
# convert tuple to list
oddList = list(oddNum)
sortedOddList = sorted(oddList)

noDuplicatesOddList = []

for num in sortedOddList:
    if num in noDuplicatesOddList:
        continue
    else:
        noDuplicatesOddList.append(num)

noDuplicatesOddTuple = tuple(noDuplicatesOddList)
print("No Odd Duplicates: ", noDuplicatesOddTuple)



#Question 7 - Create a code to find the union of two sets.

set1 = {1,2,3}
set2 = {3,4,5}
  
setUnion = set1.union(set2)
print("The union of set1 and set2 is: ", setUnion)


#Question 8 - Create a code to find the common elements between two sets of integers.

set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}

setIntersect = set_1.intersection(set_2)
print("Intersection: ", setIntersect)


# Question 9 - Generate a new set with only the even numbers from the original set using Python code.

original_set = {1, 2, 3, 4, 5, 6, 7, 8}

setEvenNumbers = set()

for num in original_set:
    if num % 2 == 0:
        setEvenNumbers.add(num)
print("Even numbers in set is: ", setEvenNumbers)



#Queston 10 - Write a code to create a dictionary from two lists, one for keys and another for values.

keys = ["name", "age", "city"]
values = ["John", 30, "New York"]

myDict = {}
for index in range(len(keys)):
    myDict[keys[index]] = values[index]
  
print("The Dictionary is: ", myDict)
