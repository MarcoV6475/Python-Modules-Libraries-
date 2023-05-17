#Marco Villegas
#5/18/23

#Problem 1
print("\n\nProgram 1 - randomrange.py")
import random as rn
for i in range(10):
    r = rn.randrange(25, 36)
    print("Random integers between 25 and 35: ", r)
#This program utilizes the Random Module and this code prints 10 random
#integers between 25 and 35.


#Problem 2
print("\n\nProgram 2 - randomint.py")
import random as rn

number = rn.randrange(0, 100+1, 2)
odd_number = number + 1
print("Odd number between 0 and 100:", odd_number)
#This program utilizes the random.randrange to print a odd number between 0-100;
#it does so by getting an even number first and then adding + 1 to it to obtain
#the odd number.


#Problem 3
print("\n\nProgram 3 - randomday.py")
import random as rn
day_list =["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("Choosing a random day of the week and it's: ",rn.choice(day_list))
#This program uses the random.choice function which it pulls info from a list,
#in this case the days of the week, and then randomly chooses a day.



#Problem 4
print("\n\nProgram 4 - pi.py")
import math
n = 1
pi = 0
for i in range(1000000):
    if i % 2 == 0:
        pi += (1 / n)
    else:
        pi -= (1 / n)
    n += 2

pi *=4
print("Example found in the internet for pi is: ",pi)

pi_module = math.pi
print("The math module's way of computing pi: ",pi_module)
#These programs uses the math module to compute pi, what I found is another way
#to do this exact same result. I found an example that uses pi and n = 1, and
#then by using and if else statement computes pi just like the math module. 



#Problem 5
print("\n\nProgram 5 - degree.py")
import math
def Convert(radian):
    pi = 3.14159
    radian = (int(input("Enter a number for radians: ")))
    degree = radian * (180/pi)
    return degree
radian = 5
print("Example found to convert radian to degrees: ", (Convert(radian)))

x = (int(input("Enter a number, so the math module can convert radians to degrees: ")))
print("Math module way to convert radians to degrees: ", math.degrees(x))
#These programs uses the math module to convert radians to degrees but I found
#another example that produces similar results. The program has pi = 3.14159 and
#then ask's the user to input a number for radians; the code then proceeds to
#multiply the radian * (180/pi) which then gives us simialr results as the math
#module. 



#Problem 6
print("\n\nProgram 6 - factorial.py")
import math
num = int(input("Enter a number to find the factorial: "))
factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1 ,num + 1):
        factorial = factorial*i
    print("Online Example - The factorial of",num,"is",factorial)
    

n = (int(input("Enter a number, so the math module can calculate the factorial: ")))
print("Math module way to calcualte a factorial: ", math.factorial(n))
#These programs use the math modules factorial function and I found an example
#that does the same as the factorial. The example I found ask the user to input
#a number, if it negative you get a response saying it does not exsit, if you
#input a 0 the answer will be 1, and if you put a other interger then it will
#calculate the factorial of that number just how the math module does.  
