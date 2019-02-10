#Exercise 16: Password Generator

#The prompt for this Exercise was to:
#Create a password generater.
#Have a mixture of lower/upper case letters, numbers and symbols
#The password should be random, generating a new password everytime the user asks
#Extra challenge:
    #Ask the user for how strong they want their password to be.
    #For weak passwords, pick a word or two from a list.
#The random module is required for this task.

import random
import string

print("Welcome to the Random Password Generator")
strongweak = input("Would you like to generate a strong or weak password? \n Type 'strong' for strong password and 'weak' for weak password': ")
if strongweak == "weak":
        weak = ["book", "salad", "bottle", "girl", "pen", "cup", "read", "stir", "orange", "lasagna", "picture", "perfume", "box", "scissors",
                "can", "phone", "smart", "apple", "samsung", "hair", "brush", "glue", "tissue", "time", "frame", "nose", "cream", "magnet", "sticker"]
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        weakpassword = [(random.choice(weak)), (random.choice(weak)), (random.choice(numbers))]
        weakpassword = "".join(map(str, weakpassword)) #"".join was used to join elements in the list to become one cohesive string
        print(weakpassword)
        
else:
    def letter_range(start="a", stop="{", step=1): #start at 'a' and stop at '{', which is right after 'z' on the ASCII table
        for ord_ in range(ord(start.lower()), ord(stop.lower()), step): #ord returns the integer value of a character on the ASCII table --> refer ORD/CHR EXAMPLE file
            yield chr(ord_)                                             #chr returns the character of an integer value on the ASCII table --> refer ORD/CHR EXAMPLE file
    def letter_range_upper(start="A", stop="{", step=1):#step = 1 means go up by one unit each time, if it was step = 2, then [a, c, e, g... etc]
        for ord_u in range(ord(start.upper()), ord(stop.upper()), step): #__.upper or __.lower just makes the result upper/lowercase
            yield chr(ord_u)#yield is basically the same as return() for a normal function
            
    stronglower = list(letter_range("a", "z"))
    strongupper = list(letter_range_upper("A", "Z"))
    strongdigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    strongsymbols =  ['@', '!', '$', '%', '^', '&', '*', '_', '-', '>', '<', '?']
    strongpassword = [(random.choice(list(letter_range("a", "z")))), (random.choice(list(letter_range("a", "z")))), (random.choice(list(letter_range("a", "z")))), (random.choice(list(letter_range("a", "z")))),
                      (random.choice(list(letter_range_upper("A", "Z")))), (random.choice(list(letter_range_upper("A", "Z")))), (random.choice(list(letter_range_upper("A", "Z")))), (random.choice(list(letter_range_upper("A", "Z")))), 
                      (random.choice(strongdigits)), (random.choice(strongdigits)), (random.choice(strongdigits)), (random.choice(strongdigits)),
                      (random.choice(strongsymbols)), (random.choice(strongsymbols)), (random.choice(strongsymbols)), (random.choice(strongsymbols))]
    
    random.shuffle(strongpassword) #learnt about the random.shuffle function here, shuffles elements in a list randomly
    strongpassword = "".join(map(str, strongpassword))#the 'map' function is used to either apply a function to all elements in a list
    print(strongpassword)                             #OR to change the item type (tuple, string, list, int... etc) 
                                                      #here I used it to change the strongpassword tuple into a string to be joined together to
                                                      #make one cohesive string rather than having seperate elements of the list being printed


#In this Section here:
#def letter_range_upper(start="A", stop="{", step=1):#step = 1 means go up by one unit each time, if it was step = 2, then [a, c, e, g... etc]
        #for ord_u in range(ord(start.upper()), ord(stop.upper()), step):
            #yield chr(ord_u)
#All it does is:
    #1. Start at "A" on the ASCII table
    #2. Convert it to its corresponding integer on the ACSII table
    #3. Then changes it back to a character --> Adding the character into the letter_range_upper function
    #4. It then moves onto the next value on the ASCII table, B
    #5. Repeats with all values

#In this exercise I got a little more comfortable with defining my own function (using def function) and made the letter_range and letter_range_upper to represent Lowercase and Uppercase letters on the ASCII table to be referred to.
#I learnt many new things like:
    #The difference between a generator function and a normal function through using yield/return
    #How to refer to the ASCII table using the ord/chr functions
    #How to make my own usable user defined functions
    #The random.shuffle function
    #The use for the map function
