#The Grandest Staircase Of Them All
#==================================

#With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

#Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options. 

#Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
#For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

###
### solution, passed all tests
###
def solution(n):
    # Avoiding the use of list comprehension for readability
    # Instantiating initial list using conditionals to account for n<3
    Coeff = []
    for c in range(n+1):
        Coeff.append(int(c == 0))
    
    # Calculating the coefficients on each polynomial in the generating function for Q(n) 
    for i in range(1,n):
        # Instantiating the list we 'build' the coefficients to write back
        Build = list(Coeff)
        # Using the base list = Coeff to build the new Build list of coefficients
        for d in range(n+1):
            if d - i < 0:
                Build[d] = Coeff[d]
            else: 
                Build[d] = Coeff[d] + Coeff[d-i]
        Coeff = list(Build)
    
    return Coeff[n]

n=5
sol = solution(n)
print (sol)