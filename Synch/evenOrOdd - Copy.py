
# Online Python - IDE, Editor, Compiler, Interpreter
#create Lists for even & odd
evenList = []
oddList = []
#print text
ENumber = "Positive number: "
ONumber = "Odd number: "
#print results
def totalNums():
    print(ENumber)
    print(evenList)
    print(ONumber)
    print(oddList)
# keep asking for a number if a number isnt entered
# while(True):
#     try:
#         N = int(input("Enter number to check if it's even"))
#         break
#     except ValueError:
#         print("not a valid number")
# #check if the number is 0 as0 is non divisable and even
# if (N == 0):
#     print("Zero is neither positive or negative")
# #Divide by 2 to find out if even or odd
# else:
#     if (N % 2 == 0):
#         print ("Your number is even!")
#         #add number to list and run print fuction
#         evenList.append(N)
#         totalNums()
#     else:
#         print("Your number is odd...")
#         oddList.append(N)
#         totalNums()


def numCheck():
    # keep asking for a number if a number isnt entered
    while(True):
        try:
            N = int(input("Enter number to check if it's even"))
            break
        except ValueError:
            print("not a valid number")
            #check if the number is 0 as0 is non divisable and even
    if (N == 0):
        print("Zero is neither positive or negative")
            #Divide by 2 to find out if even or odd
        numCheck()
    else:
        if (N % 2 == 0):
            print ("Your number is even!")
        #add number to list and run print fuction
            evenList.append(N)
            totalNums()
            numCheck()
        else:
            print("Your number is odd...")
            oddList.append(N)
            totalNums()
            numCheck()


# Start program
numCheck()






# print("Positive numbers: ")
# print(pList)
# print("Negitive numbers: ")
# print(nList)





# def sum(a, b):
#     return (a + b)

# a = int(input('Enter 1st number: '))
# b = int(input('Enter 2nd number: '))

# print(f'Sum of {a} and {b} is {sum(a, b)}')
