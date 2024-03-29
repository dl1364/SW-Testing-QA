'''
Name: Deven Lee
NetID: dl1364  
Date: 3/7/23
'''

def calculateBMI(feet, inches, weight):
    newWeight = weight * .45
 
    addInches = feet * 12
    newInches = inches + addInches
    
    newHeight = newInches * .025
    squareHeight = newHeight * newHeight
    
    BMI = newWeight / squareHeight
    roundBMI = round(BMI)
    print("The BMI for a person who is", feet,"'",inches, "and weighs",weight, "lbs is","%.2f" % BMI, "or pratically,", roundBMI)
    if(BMI < 18.5 and BMI > 0):
        print("Category: Underweight\n")
    elif(BMI > 18.5 and BMI < 24.9):
        print("Category: Normal Weight\n")
    elif(BMI > 25 and BMI < 29.9):
        print("Category: Overweight\n")
    elif(BMI >= 30):
        print("Category: Obese\n")
    elif(BMI < 0):
        print("Error unreal value please try again.\n")
        return
    print("Do you wish to exit the program?")
    print("Yes or No?")
    leave = input("Input: ")
    print("\n")
    if(leave == "y" or leave == "Y" or leave == "Yes" or leave == "yes"):
        print("Exiting Program..")
        exit()
    elif(leave == "n" or leave == "N" or leave == "No" or leave == "no"):
        return
    
    
    
    

condition = True
while(condition):
    print("BMI Calculator\n")
    
    print("Please enter your height in feet and inches")
    print("Example: 5 11\n")
    feet, inches = input("Input: ").split()
    print("\n")
    newfeet = int(feet)
    newinches = int(inches)
    print("Please enter weight in pounds\n")
    weight = input("Input: ")
    newweight = int(weight)
    print("\n")
    calculateBMI(newfeet, newinches, newweight)
    
    
    
