#Now an introduction to randomness (this is a comment by the way), these do not
#affect the code in any way, they are just descriptive text


from random import * #this is an important line included to help you on your way


'''There are many simple programs that require an element of randomness.
    For example, simulating the role of a die is difficult if the numbers that 
    appear on each role are built into the code. However, computers and people
    have a hard time acting in a truly random fashion. Early programmers had
    to get very creative to even "fake" random number generation.
    (this is also a comment, a \#\ is a one line comment while triple quotes 
    allow for longer comments by using a string format)
    
'''
def main():
    #if we set the number that show up each time we "roll the die" we would not
    #be able to get any randomness
    print("We rolled a 5! (again)")
    #we will alwoys print 5 when this program is run
    #replace this comment with your random number printer!
    
    return 0 #this is a return statement, we'll be seeing this alot so I'll explain later
    


    
#The if statement below is a weird python thing. We can ignore it for now
'''If you need to know what this is, it would be easiest to describe as an
    invocation statement. Python is a scripting language, so functions like 
    \main\ arent run by default. This statement tells python to run the
    defined function above in the given sequence.
'''
if __name__ == '__main__':
    main()