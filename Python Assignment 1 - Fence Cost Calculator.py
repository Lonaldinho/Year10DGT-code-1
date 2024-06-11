# Fencing Calculator
# Author: Logan Kim
# Date 22/05/2024
# Version 1
print("Instruction")
print()
print("Price of fencing per meter")
print("Then input the length and width")
print("This program will print the cost of fencing")
print()
number=""
def number_check(questions):
    error = "Put in a number bigger than zero\n"
    while True:
        try:
            number=float(input(questions))
            if number>0:
                return number
            else:
                print(error)
        except ValueError:
            print(error)
keepgoing="Y"
while keepgoing =="Y":
    price= number_check("$price per meter")
    width = number_check("width ")
    height= number_check ("height ")
    perimeter= (width+height)*2
    cost=(perimeter)*price
    print(f"fencing cost for your land: = ${cost}")
    keepgoing = input ("Coontinue? Y/N ")
    if keepgoing!=("N"):
        keepgoing="Y"
print("Thank you for using this program")
        

