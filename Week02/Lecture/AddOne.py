# This reads in a number and then adds 1 to it and prints it out on screen
# Author: Eddie Callan (G00398815)

#The line below looks for the user to input a number and saves it in the variable 'number' as an integer (as a string cannot be used for the calcuation later on)
number = int(input ('Please enter a number:'))
#The line below creates a new varaible named newnumber using the value of the variable number and adding 1 to it
newnumber = number + 1
#The line below prints out the text "Plus one is:" and also prints out the value of the varuable 'newnumber'
print('{} Plus one is: {}' .format(number, newnumber))