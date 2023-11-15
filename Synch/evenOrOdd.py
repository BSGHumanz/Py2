
# Online Python - IDE, Editor, Compiler, Interpreter
#create Lists for even & odd
pList = []
nList = []
#print resaults
def totalNums():
    print("Positive numbers: ")
    print(pList)
    print("Odd numbers: ")
    print(nList)
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
else:
    if (N % 2 == 0):
        print ("Your number is even!")
        #add number to list and run print fuction
        pList.append(N)
        totalNums()
    else:
        print("Your number is odd...")
        nList.append(N)
        totalNums()

# print("Positive numbers: ")
# print(pList)
# print("Negitive numbers: ")
# print(nList)





# def sum(a, b):
#     return (a + b)

# a = int(input('Enter 1st number: '))
# b = int(input('Enter 2nd number: '))

# print(f'Sum of {a} and {b} is {sum(a, b)}')
