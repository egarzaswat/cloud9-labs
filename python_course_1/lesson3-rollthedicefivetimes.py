#Now that we've rolled the die once, we want to roll the die alot
#lets make this easier by rolling the die multiple times in a single run
#in fact, lets have it spin forever!


from random import *



'''
    Simple programs often provide a function that we want to run multiple times
    An easy way to do this is to create a \loop\ that runs a specified bit of
    code for as many times as we want (in this case 5 times) lets role the dice
    
'''
def main():
    #try putting your loop here
    print ("We've rolled a {0}!".format(randint(1,6)));
    
    return 0
    


    
#The if statement below is a weird python thing. We can ignore it for now
'''If you need to know what this is, it would be easiest to describe as an
    invocation statement. Python is a scripting language, so functions like 
    \main\ arent run by default. This statement tells python to run the
    defined function above in the given sequence.
'''
if __name__ == '__main__':
    main()