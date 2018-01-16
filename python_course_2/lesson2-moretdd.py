"""As you can see from the program below, I also made a program to complete
   the last lab. You probably won't like my solution, but it does pass the TESTS
   which is all that matters in TDD. This may seem to run against writing quality
   code, but it ensures the developer doesn't spend any more time in development
   than necessary and new requirements can always be added that improve on
   the base design. Never fear! If you did the last lab properly, then you'll have
   no problem with my additional test"""
   
   
   #cyphers take an input and scramble it to generate an output that is encoded
   #cyphers should normally be reversible, but you should only focus on ensuring
   #YOUR chosen cypher method produces the outputs expected
   
   
def main(input):
    print("Here is what I started with: ", input)
    #input is what I am sending in via the tests below
    #check the assertions below to see what each message should become when returned
   
    return "hplolr lv wkh ehvw" #stretching the bounds of "technically" correct
   
if __name__ == '__main__':
    encryptedVal = main("emilio is the best")
    assert(encryptedVal == "hplolr lv wkh ehvw")
    print("You would have passed the last lab here!")
    encryptedVal = main("tom is terrific")
    assert(encryptedVal == "wrp lv whuulilf")
    print("You passed the new requirements as well!")
  