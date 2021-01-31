# This reads in a users height and weight and calulates their BMI
# Author: Eddie Callan (G00398815)

# The line below looks for the user to input their height and saves it in variable 'height' as an integer

height = int(input("Please enter your height in centimeters: "))

# The line below looks for the user to input their weight and saves it in the variable 'weight' as an integr
weight = int(input("Please your weight in kilograms: "))

# The line below displays the BMI for the user dividing the weight by height by height and then mutiplyng my 10000 (for cm to meteres squared)

print("The  exact BMI is ", weight / (height * height) * 10000)
