import math
import random

def guess(l,u):

    if l > u:
        print("Please enter the maximum number which is greater than minimum nummber ")
    else:
        res=random.randint(l,u)
        n=round(math.log((u-l+1),2))
        print("You have"+" " + str(n) +" " + "chances to guess the correct number")
        for i in range(n):
            g=int(input("Enter your guess number:"))
            if g >=l and g<=u:
                if g < res:
                    print("Your guessed number is too small!")
                    i = i + 1
                elif g > res:
                    print("Your guess number is  too large")
                    i = i + 1
                elif g == res:
                    print("Congratulations you have guessed the number in" + " " + str(i + 1) + " " + "times" + " " +"\U0001F929")
                    break
            else:
                print("Enter the number which is in range of minimum and maximum")
                break


        else:
            print("Your chances are completed better luck next time!!"+ " "+"\U0001F642")


l=int(input("Enter the minimum number:"))
u=int(input("Enter the maximum number: "))
guess(l,u)






