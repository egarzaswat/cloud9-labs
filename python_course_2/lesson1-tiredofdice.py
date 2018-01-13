"""I'm tired of dice. Lets try some cyphers this time! 
   We're going to start introducing TEST DRIVEN DEVELOPMENT
   concepts into labs now. Basically, TDD is a development method that
   relies on pre-defined tests to guide program writing. 
   Write a cypher that takes the values I input and spits out the values I expect."""
   
   
   #cyphers take an input and scramble it to generate an output that is encoded
   #cyphers should normally be reversible, but you should only focus on ensuring
   #YOUR chosen cypher method produces the outputs expected
   
   
def main(input):
    print("Here is what I started with: ", input)
    #input is what I am sending in via the tests below
    #check the assertions below to see what each message should become when returned
   
    return -1 #standard "I don't work" return value
   
if __name__ == '__main__':
    encryptedVal = main("emilio is the best")
    assert(encryptedVal == "hplolr lv wkh ehvw")
    #quick explaination an "assert" requires that the statement within the 
    #parentheses be true, otherwise, the program fails this is a simple way to 
    #test programs in python
    #more formal testing would be done in separate files and run whenever an
    #application was deployed or setup on a new machine
    print("You Passed!!!")
  