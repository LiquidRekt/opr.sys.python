"""
Author: Thomas.JR
THMS OPERATING SYSTEM
version: pre-alpha v.0.0.001
"""

#program functions
def iSolver():
  #variable
  hello = "\nHi! Welcome to iSolver!"
  greeting = "\nChoose the experession that linked to numbers to solve! \n   (1) (x+y+z)^2 \n   (2) (x+y)^n \n   (3) ((x^2)-x)/(n-x) \n   (4) x^3 + y^3 + y^2"


  #functions
  def experession1(): #(x+y+z)^2
    x = int(input("-------\nType x:"))
    y = int(input("-------\nType y:"))
    z = int(input("-------\nType z:"))
    p = "(%d + %d + %d)^2" % (x,y,z)
    onesum = (x+y+z) ** 2
    print("------------------------------------------------------\nExpression 1: %s \n Input x,y,z respectively: %d, %d, %d \n Value of experession: %d" % (p,x,y,z,onesum))
    print("-------------------------------")
    finisher()
  
  def experession2(): #(x+y)^n
    x = int(input("-------\nType x:"))
    y = int(input("-------\nType y:"))
    n = int(input("-------\nType exponent number:"))
    p = "(%d + %d)^%d" % (x,y,n)
    twosum = (x+y) ** n
    print("------------------------------------------------------\nExpression 2: %s \n Input x,y respectively: %d, %d \n Exponent: %d \n Value of experession: %d" % (p,x,y,n,twosum))
    print("-------------------------------")
    finisher()
  
  def experession3(): # ((x^2)-x)/(n-x)
    x = int(input("-------\nType x:"))
    n = int(input("-------\nType n:"))
    if (x == n):
      print("SystemError: This will lead to division by zero! \n")
      print("-------------------------------------")
      finisher()
    else:
      p = "((%d^2)-%d)/(%d-%d)" % (x,x,x,n)
      threesum = ((x ** 2) - x)/(n-x)
      print("------------------------------------------------------\nExpression 3 %s \n Input x,n respectively: %d, %d \n Value of experession: %d" % (p,x,n,threesum))
      print("-------------------------------")
      finisher()
   
  def experession4(): # x^3 + y^3 + z^3
    x = int(input("-------\nType x:"))
    y = int(input("-------\nType y:"))
    z = int(input("-------\nType z:"))
    p = "%d ^ 3 + %d ^ 3 + %d ^ 3" % (x,y,z)
    foursum = x**3 + y**3 + z**3
    print("------------------------------------------------------\nExpression 2: %s \n Input x,y respectively: %d, %d, %d \n Value of experession: %d" % (p,x,y,z,foursum))
    print("-------------------------------")
    finisher()   

  def finisher():
    command = str(input("Execute: \n  try_again : if you want to try this expression again \n  try_other: if you want to try another expression \n  exit: if you don't want to calculate any more \n \n >>>"))
    if (command == "try_again"):
      experession3()
    elif (command == "try_other"):
      print("-------------------------")
      main()
    elif (command == "exit"):
      exIt()
      
  def sTaRt():
    greeTer()
    kUrso()
      
  def kUrso():
    stringTo = str(input("\n>>> "))
    if (stringTo == "calExper"):
      main()
    else:
      print("Function undefined.\n")
      liSt()
      kUrso()
  
  def liSt():
    print("What do you want to do?\n  -calExper: Calculate listed experessions.")
      
  def greeTer():
    print(hello)
    liSt()
    
      

  def main(): # main function
    print(greeting)
    exchoice = int(input("Choose the type of experession you want to solve\n>>> "))
    if (exchoice == 1):
       experession1()
    elif (exchoice == 2):
       experession2()
    elif (exchoice == 3):
       experession3()
    elif (exchoice == 4):
       experession4()
    else:
       print("Experession unavailable!")
       errorStartAgain()
       
       
  def errorStartAgain():
     excher = int(input("Please type the number that represents the experession in the list! \n"-------------------------"\n>>> "))
     if (excher == 1):
       experession1()
     elif (excher == 2):
       experession2()
     elif (excher == 3):
       experession3()
     elif (excher == 4):
       experession4()
     else:
       print("Experession unavailable!")
       errorStartAgain()
       
  def exIt():
    print("Thanks for using our product!")
    mainIe()
  
       

 

  #Start
  sTaRt()
  
#variables
cRedits = "THMS OPERATING SYSTEM \nCopyright 2017, Thms Studios.\nVersion: pre-alpha v.0.0.001"


#system information
print(cRedits)
  

#system functions

def mainIe():
   start = str(input("\nC:\THMS >>> "))
   if (start == "prg(iSolver)" or start == "iSolver"):
     iSolver()
   elif (start == "shutdown"):
     shutDown()
   else:
     print("'%s' is not recognized as an internal or external command, operable program or batch file !" % (start))
     mainIe()
     
def shutDown():
  print("Goodbye!")
   

#user command input
mainIe()

  
  
  
  
  
  
  
  
  
  
