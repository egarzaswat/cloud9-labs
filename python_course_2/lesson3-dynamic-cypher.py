"""Now, a fixed cypher is fairly easy to figure out, but a cypher that can change based
   on the values that the user inputs gives the tool more flexibility. The main
   function now includes a number that will be used to manipulate the given text
   to create the desired output."""
   
   
   #cyphers take an input and scramble it to generate an output that is encoded
   #cyphers should normally be reversible, but you should only focus on ensuring
   #YOUR chosen cypher method produces the outputs expected
   
   
def main(input, manipulator):
    print("Here is what I started with: ", input)
    #input is what I am sending in via the tests below
    #check the assertions below to see what each message should become when returned
   
    return "hplolr lv wkh ehvw" #stretching the bounds of "technically" correct
   
if __name__ == '__main__':
    encryptedVal = main("emilio is the best",3)
    assert(encryptedVal == "hplolr lv wkh ehvw")
    encryptedVal = main("tom is terrific",3)
    assert(encryptedVal == "wrp lv whuulilf")
    encryptedVal = main("emilio is the best",5)
    assert(encryptedVal == "jrnqnt nx ymj gjxy")
    encryptedVal = main("alan is terrible",8)
    assert(encryptedVal == "itiv qa bmzzqjtm")
    print("You made a great cypher! Congratulations!!!")
    
  