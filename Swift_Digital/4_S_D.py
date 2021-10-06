#function to count numbers of climbing options
def findStep(n) :

    if (n == 1 or n == 0) :
        return 1

    elif (n == 2) :
        return 2

    else :
        return findStep(n - 2) + findStep(n - 1)
 
 
# Driver code

n = int(input("Enter number of stairs: "))
# If n = 3 then the number of climbing options is 3
# because {1 + 1 + 1 = 3; 2 + 1 = 3; 1 + 2 = 3}
print("Number of options for climbing stairs: ",findStep(n))
#Master of R_Grigla 