"""There are three main schools of programming. Procedural, Object-Oriented, and
Functional. Each come with their own strengths and weaknesses and are a different
way of creating an application. Another way of thinking of these three schools is
that they are attempting to define the world in three different ways. I like
that approach, so that's how I'll write about them.

Procedural programming defines the world as a series of steps or a RECIPE to turn
a given thing into something else. The prior lessons fall into this school of 
programming and is a common entry point into programming. Python is, first and
foremost, a scripting language. However, it allows for a programmer to use an
OBJECT-ORIENTED approach as well.OBJECT

Object-Oriented programming defines the world as an assortment of objects, 
self-contained entities, that interact with each-other in various ways. This is 
one of the more common forms of programming in commerical companies due to its
strengths. That is the next school of programming that we'll explore in this lab
"""

class Rectangle: 
    #a class is the blueprint for an object. this was a hard concept for me when
    #I began programming, since it is a fundamental change in thinking about 
    #programming from a procedural approach. I think the confusion with me was 
    #resolved when I realized that classes dont actually DO anything whereas
    #a procedural program DOES do something. A class is the script that an object
    #follows during its interaction in a way, a class is like the script for a
    #play and the objects are the actors on stage enacting the play. Ideally,
    #each actor will say a line that will prompt a line from another actor
    #objects work much the same way. As a developer, you are scripting the 
    #interactions between objects instead of scripting the entire play
    
    shortSide = 5;#length of a rectangle's short side
    longSide = 8;#length of a rectangle's long side
    
    def __init__(self,shortSide,longSide):
        #the __init__ function is a special function that tells the object how
        #to create itself. To use the actor analogy, it is like the bio of a 
        #character, the bio tells the actor the basic information to "become" a
        #given character. This actor will become the rectangle
        
        #I'm tired, check back later for the conclusion or hound me if I get lazy
        #IN the meantime!!!
        return 0;