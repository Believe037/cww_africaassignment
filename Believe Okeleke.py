# QUESTION 1: VARIABLES

#Q.1.a - Assign the value 10 to variable and print it
x = 10
print(x)

#Q.1.b - Assign the value "Hello" to a variable message and print it.
message = 'Hello'
print(message)
    
#Q.1.c - Create a variable and assign it a value.
color = 'darkblue'
    
#Q.1.d - Print the variable.
print(color)
    
#Q.1.e - Print the type of the variable.
print(type(color))
        
        

# QUESTION 2: DATA TYPES
    
#Q.2.a - Create a variable of each of the following data types: integer, float,
    
#integer
y = 33
            
#float
b = 3.3
            
#string
firstName = 'Believe'
            
#boolean
condition = True
        
#Q.2.b - Print the value of each variable and the data type.
print(y)
print(type(y))
        
print(b)
print(type(b))
        
print(firstName)
print(type(firstName))
        
print(condition)
print(type(condition))
    
#Q.2.c - Convert each variable to a different data type and print the value.
    
# convert integer to float
yFlt = float(y)
print(yFlt)
        
#convert float to integer
bInt = int(b)
print(bInt)
        
#convert string to boolean
firstNameBool = bool(firstName)
print(firstNameBool)
        
# convert boolean to string
conditionStr = str(condition)
print(conditionStr)
    
    
#Q.2.d - print the data types of each of the Convert variable
    
print(type(yFlt))
print(type(bInt))
print(type(firstNameBool))
print(type(conditionStr))



# QUESTION 3: SETS

#Q.3.a - Create a set of numbers from 1 to 10.
numbers = {1,2,3,4,5,6,7,8,9,10}
    
#Q.3.b - Add the number 11 to the set.
numbers.add(11)
print(numbers)
    
#Q.3.c - Remove the number 5 from the set.
numbers.remove(5)
print(numbers)
    
#Q.3.d - Check if the number 3 is in the set.
checkfor3 = 3 in numbers
print(checkfor3)
    
#Q.3.e - Print the size of the set.
print(len(numbers))
    
    
    
# QUESTION 4: LISTS
    
#Q.4.a - Create a list of the numbers from 1 to 10.
list = [1,2,3,4,5,6,7,8,9,10]
    
#Q.4.b - Add the number 11 to the list.
list.append(11)
print(list)
        
#Q.4.c - Remove the number 5 from the list.
list.remove(5)
print(list)
    
#Q.4.d - Check if number 3 is in the list.
chckfor3 = 3 in list
print(chckfor3)
    
#Q.4.e - Remove the first element from the list.
list.pop(0)
print(list)
    
#Q.4.f - Print the size of the list
print(len(list))
    
#Q.4.g - Reverse the order of the list
list.reverse()
print(list)


#QUESTION 5: TUPLES
    
#Q.5.a - Create a tuple of the numbers from 1 to 10.
myTuple = (1,2,3,4,5,6,7,8,9,10)
    
#Q.5.b - Print the tuple.
print(myTuple)
    
#Q.5.c - Check if the number 3 is in the tuple.
checkfor_3 = 3 in myTuple
print(checkfor_3)
    
#Q.5.d - Try to add a number to the tuple
# myTuple[10] = 11


#QUESTION 6: DICTIONARIES
    
#Q.6.a - Create a dictionary person with the keys 'name', 'age' and 'country'. Assign appropriate values.
person = {"firstName": 'Believe', 
                  "age": 33, 
                  "country": 'Nigeria'
                  }
        
#Q.6.b - Print the value associated with the keys 'age'.
print(person['age'])
    
#Q.6.c - Update the value associated with the key 'country' to a new country.
person['country'] = 'Canada'
    
#Q.6.d - Print the dictionary.
print(person)
    
#Q.6.e - Add a new key-value pair to dictionary.
person['lastName'] = 'Okeleke'
print(person)
    
#Q.6.f - Remove a key-value pair from the dictionary.
person.pop('country')
print(person)



#QUESTION 7: MATHEMATICAL OPRATION 

#Q.7.a - Create two variables a and b and assign them any numericalvalues.
a = 2
b = 3
    
#Q.7.b - Add a and b, and print the result.
sum = a + b
print(sum)
    
#Q.7.c - Multiply a and b, and print the result.
product = a * b
print(product)
    
#Q.7.d - Add, subtract, multiply, and divide two numbers.
4 + 5
10 - 7
2 * 3
5 / 2
    
#Q.7.e - Find the remainder of a division operation.
10 % 2

#Q.7.f - Raise a number to a power. 
print(2**2)

#Q.7.g - Find the square of a number.   
num = 25
sqrt = pow(num, 0.5)
print(int(sqrt))


#QUESTION 8: CASTING

#Q.8.a - Assign a number as a string, such as "5", to a variable num_str.
num_str = '23'

#Q.8.b - Convert num_str to an integer and print the result.
int(num_str)
print(int(num_str))

#Q.8.c - Convert num_str to a float and print the result.
float(num_str)
print(float(num_str))


