def addNum(num1, num2):#create function to add numbers
    y = num1 + num2#create variable to store data
    return y#return answer

def subtractNum(num3 , num4):#create function to subtract numbers
    z = num3 - num4#create variable to store data
    return z#return answer

def multiplyNum(num5, num6):#create function to multiply numbers
    x = num5 * num6#create variable to store data
    return x#return answer

def divideNum(num7, num8):#create function to divide numbers
    w = num7 / num8#create variable to store data
    return w#return answer

def choice():#create function to choose function
    print("1 = Choose option 1 to add numbers")
    print("2 = Choose option 2 to add numbers")
    print("3 = Choose option 3 to add numbers")
    print("4 = Choose option 4 to add numbers")
    print("5 = Choose option 5 to exit program")
choice()#call function
choice = " "
while choice != "5":#while loop to pick funciton
    choice = input("Please pick a option you want to do:")
    if choice == "1":
        num1 = int(input("Please insert your first number:"))
        num2 = int(input("Please insert your second number:"))
        print("The sum of your numbers is: " + str(addNum(num1, num2)))
    elif choice == "2":
        num3 = int(input("Please insert your first number:"))
        num4 = int(input("Please insert your second number:"))
        print("The subtraction of your numbers is: " + str(subtractNum(num3 , num4)))  
    elif choice == "3":
        num5 = int(input("Please insert your first number:"))
        num6 = int(input("Please insert your second number:"))
        print("The multiplication of your numbers is: " + str(multiplyNum(num5, num6)))

    elif choice == "4":
        num7 = int(input("Please insert your first number:"))
        num8 = int(input("Please insert your second number:"))
        print("The division of your numbers is: " + str(divideNum(num7, num8)))
    else:
        print("There is no so option!")
