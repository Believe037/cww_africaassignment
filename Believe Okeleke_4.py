from module import add, subtract, multiply, divide


while True:

  try:
    a = int(input("Please enter the first number: "))       
    b = int(input("Please enter the second number: "))
  except ValueError:
     print("Not a valid input! Input must be an integer!")
     continue
  else:
     break 
  

operator = 0

# Let check for errors, incase user inputs wrong operator value
while operator <= 0:
  operator = int(input("Please select an operation: \n1. Addition, \n2. Subtraction \n3. Multiplication \n4. Division\n************************************************************** \nEnter your choice(1,2,3 or 4): "))
  if operator <= 0 or operator > 4:
    print('Sorry invalid operation value')
  else:
    if operator == 1:
      print("Your result is: ", add(a,b))
    elif operator == 2:
      print("Your result is: ", subtract(a,b))
    elif operator == 3:
      print("Your result is: ", multiply(a,b))
    else:
      # check for Zero errorDivision
      if b == 0:
        print('Sorry cannot divide by zero')
      else:
        print("Your result is: ", "{:.2f}".format(divide(a,b)))


  


