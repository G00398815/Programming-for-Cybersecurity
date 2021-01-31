# This reads in a name and then prints it out prefixed with a greeting on screen
# Author: Eddie Callan (G00398815)

# The line below looks for the user to input their name and saves it in the variable 'name'
name = input("Please enter your name:")

# The line below prints out the greeting "Hello" followed by the contents of the variable 'name' and then the text "nice to meet you"
print('Hello {}\nNice to meet you'.format(name))

# The line below looks for the user to input their age and saves it in the variable 'age'
age = int(input('Please enter your age:'))

# The line below prints out the text "Hello" and the contents of the variable 'name' and then prints out the text "Your age is" followed by the contents of the variable 'age'
print("Hello "+ name + ' Your age is: {}'.format (age))


