#Tired of the standard 6 sided die? Lets make more dice!


from random import *



'''
    Larger programs often require a sort of user menu. Modern websites
    are mainly menus that allow a user to choose what data to send and
    receive. In order for the user to choose how many sides their die should
    have, we'll be making a basic menu that will take a user choice and use
    that choice to alter your random number generator. This will be our first
    multi-function program as well.
'''

def roll_the_die(sides):
    #the old line for reference is included below
    #print ("We've rolled a {0}!".format(randint(1,6)));
    return #this program doesn't need to return anything, but it is good practice
    #to add a return to a python program to mark the program's end
    
def main():
    #you will want to place your menu here within the loop
    roll_the_die(6)#example invocation of the above function
    return 0
    


    
#The if statement below is a weird python thing. We can ignore it for now
'''If you need to know what this is, it would be easiest to describe as an
    invocation statement. Python is a scripting language, so functions like 
    \main\ arent run by default. This statement tells python to run the
    defined function above in the given sequence.
'''
if __name__ == '__main__':
    main()