
# Question 1 - Reverse the INPUT string and print result.

print("*******************************************\n Hello, Welcome to my First Python Program!.\n*******************************************")

strng = ""

while len(strng) >= 0:
    strng = input("Please enter your String: ")
    
    str(strng)
    if strng.isspace() or len(strng) == 0:
      print('Sorry, empty input or only whitespace NOT ALLOWED 🚫🚫🚫! TRY AGAIN!!!!')
      continue
      
    else:
      strngRev = strng[::-1] #This reverses the strng input

      #QUESTION 1
      print("Reversed string:  ", strngRev)
      wordList = strng.split(" ") #converts the string into a list.
      wordList.sort() #sort the list in ascending order
      wordList.sort(key=len) # sorts the list according to highest length

      # QUESTION 2
      #the longest string is the last index on the list
      print("Longest word: ", wordList[len(wordList) - 1])

      #QUESTION 3
      #the shortest word is the first index on the list
      print("Shortest word: ", wordList[0])

      char = ""
      # A while put to handle empty input and whitespaces
      while len(char) >= 0:
        
        #this includes all uppercase character to the char count.
        sentence = strng.lower() 
        char = input("Enter a character to count its occurrences:  ").lower()
        str(char)

        if char.isspace() or len(char) == 0:
          print('Sorry, empty input or only whitespace NOT ALLOWED 🚫🚫🚫! TRY AGAIN!!!!')
          continue
        else:
          charCount = 0
          for item in sentence:
            if item == char:
              charCount += 1
          
          # QUESTION 4
          print(charCount)

          #This ends the while loop of the occurrence input error, after valid input is given.
          break 

      #This ends the while loop of the string sentence input error, after a valid input is given.
      break 



