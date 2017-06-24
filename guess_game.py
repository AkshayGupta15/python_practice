import time
from random import randint
def initl():
    msg=" You can't beat me!!!  "
    print " ^-^ "*5,"Welcome to GUESS THE NUMBER"," ^-^ "*5
    
    time.sleep(1)
    usr_name=raw_input("Enter your name: ")
    print 'Hello!',usr_name
    time.sleep(1)
    print "-"*20
    print "Let's play Guess the number:"
    time.sleep(1)
    print "Rules are simple :"
    time.sleep(1)
    print "I'll think of a number between 0 to 9 and you have to guess that in 3 chances."
    print "-"*20
    print "\n"
    time.sleep(2)
    return 0




initl()
dummy=raw_input("Press ENTER key to begin\n")
print "Let me Pick a number....\n"
msg=" \n You can't beat me!!! My number was:  "
chance=3
show=3
number=randint(0,9)
time.sleep(1)
print "******OK, I have a number*****\n"
time.sleep(1)
while chance:
    print"."*50,"\n"
    #print "Guesses remaining",chance-1
    gues=int(raw_input("Enter your Guess: "))
    
    if gues == number:
        msg = "\nDamn it! You won this time my number was:  "
        break
    elif gues > number :
        time.sleep(0.5)
        print "\n=>Come DOWN a little bit.\n"
        time.sleep(1)
        print "Guesses remaining:",chance-1
        time.sleep(0.5)
        chance=chance-1  
    else:
        time.sleep(0.5)
        print "\n=>Go UP a little bit.\n"
        time.sleep(1)
        print "Guesses remaining:",chance-1
        time.sleep(0.5)
        chance=chance-1

print"."*50        
print msg,str(number)  


        
