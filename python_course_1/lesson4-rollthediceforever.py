#Now that we've rolled the die once, we want to roll the die alot
#lets make this easier by rolling the die forever in a single run


from random import *



'''
    This one is similar to the last guy, but we want to run this forever
    To do this, we want to use a different kind of loop.
    We also want to set this program up where each role is initiated by pressing
    the enter key
'''
def main():
    #try putting your loop here
    print ("We've rolled a {0}!".format(randint(1,6)));
    #add your enter key prompt here (make sure its in the loop)!
    return 0
    


    
#The if statement below is a weird python thing. We can ignore it for now
'''If you need to know what this is, it would be easiest to describe as an
    invocation statement. Python is a scripting language, so functions like 
    \main\ arent run by default. This statement tells python to run the
    defined function above in the given sequence.
'''
if __name__ == '__main__':
    main()