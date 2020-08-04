import time as t
import string
import random
from itertools import product


def crack_password(pw):
    pw = str(pw)
    time = t.time()
    length = len(pw)
    available_chars = []
    
    ##put in lowercase letters
    for char in string.ascii_lowercase:
        available_chars.append(char)
        
    ##same for uppercase letters
    for char in string.ascii_uppercase:
        available_chars.append(char)
        
    ##digits
    for digit in string.digits:
        available_chars.append(digit)
    
    ##punctuation
    for punctuation in string.punctuation:
        available_chars.append(punctuation)
        
    ##construction of all possible passwords of size of len(pw)
    available_passwords = []
    
    for item in product(available_chars, repeat=length):
        password = item[0]
        for i in range(1,length):
            password+=item[i]
        available_passwords.append(password)
    
    ##initial guess (random), delete it from available_passwords
    
    password_guess = random.choice(available_passwords)
    del available_passwords[available_passwords.index(password_guess)]
    
    guesses = 1
    
    while(password_guess != pw):
        
        password_guess = random.choice(available_passwords)
        del available_passwords[available_passwords.index(password_guess)]
        guesses+=1
        
        if(guesses%10000==0):
            print('Passing guess number '+str(guesses))
        
    
    
    
    time_it_took = t.time()-time
    
    
        
    return 'Your password, '+str(pw)+', took '+str(time_it_took)+' seconds to crack after '+str(guesses)+' guesses.'

mypassword = str(input("Enter a password: "))
print(crack_password(mypassword))

