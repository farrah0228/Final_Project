import random

def password_func(length, amount):
    """This method is to randomly chooses characters to create passwords with a given  
    length and given amount
    
    Parameters
    ----------
    length : int
        The first number, that gives length of password. 
    amount : int 
        The second number, that gives amount of many passwords will be produced.
    """
    
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
    lists=[]
    
    #give the password a range for how many characters and options it should have
    #randomly choose characters from the string of chars then append it to list called list
    for p in range(length):
        password = ''
        for c in range(amount):
            password += random.choice(chars)
        lists.append(password)
    
    #for every item that was appended into lists, print out the password    
    for item in lists:
        print("Your password is:" , item)
    return password
        
#this encoded function was taken from COGS18
def encoded_program(input_message):
    """Encodes an input message
    
    Parameters
    ----------
    input_message : string
        String to convert to code
    
    Returns
    ------- 
    encoded : string
        a string containing the encoded/converted message from input_message
    """
    
    key = 130
    encoded = ''
    #change every character in a string to a number value using ord and add a key value
    #change back to character value using chr()
    for character in input_message:
        x = ord(character) + key
        encoded = encoded + chr(x)
    print("Encoded: ", encoded)
    return encoded

#this decoded function was taken from COGS18
def decoded_program(input_secret):
    """Decodes an input secret
       Parameters
       ----------
        input_secret : string
            string to decode the encoded string
        Returns
        ------- 
        decoded : string
            a string containing the decoded message from input secret
    """
    
    key = 130
    decoded =""
    #change every character in a string to a number value using ord and subtract a key value
    #change back to character value using chr()
    for character in input_secret:
        x = ord(character) - key
        decoded = decoded + chr(x)
    print("Decoded: ", decoded)
    return decoded

def topic_generator():
    """main function that runs the topic generator"""
    #infinitely will ask user to choose a topic until a correct input is made
    #an error message will show prompting user to choose again, if incorrect number is pressed
    running = True
    while running:
            choose_topic= input("Choose a topic from this menu: \n"
                                    "Press 1 to generate a password \n"
                                    "Press 2 to encrypt a message \n"
                                    "Press 3 to decrpyt a secret message \n"
                                    "Press 4 to quit program\n" ) 
            if choose_topic == '1':
                topic_1()
     
            elif choose_topic == '2':
                topic_2()
            
            elif choose_topic == '3':
                topic_3()
            elif choose_topic == '4':
                running = quit()
            else:
                print("Error. Please choose a topic by entering a number that is 1-4")
                
                
def topic_1():
    """
    This function asks for user to input the desired length and amount of passwords. It
    also calls on the password_func to perform this function.
    """
    
    length = input('How many characters long would you like your password to be? ')
    
    #will indefinitly ask for user for length of password until an number is an input
    #an error message will show prompting user to choose again, if anything but an int pressed,
    while not length.isnumeric():
        print("Invalid number. Please input a number for a desired pathword length.")
        length = input('How many characters long would you like your password to be? ')
    amount = input('How many different password options would you like? ')  
    
    #will indefinitily ask for user for an amount of passwords until a number is an input
    #an error message will show prompting user to choose again, if anything but an int pressed,
    while not amount.isnumeric():
        print("Invalid number. Please input the number of passwords you would like.")
        amount = input('How many different password options would you like? ')
    
    #changes string to an int so it run in password_func()
    length = int(length)
    amount = int(amount)
    password_func(amount,length)
    

def topic_2():
    """
    This function asks for user to input a message they would like to encode and if they 
    would like to decode their message or to return to the topic menu. It also calls on the 
    encoded_program and decoded program to perform this function 
    """
    
    input_message = input('What message would you like to encode? ')
    output_encoded = encoded_program(input_message)

    input_decoded = input("Would you like to check if your message can be decoded? \n" 
                          "Press 1 for yes to continue \n" 
                          "Press 2 for no to go back to topic menu \n")
    
    #will indefinitily ask user for input until 1 or 2 is the input
    # an error message will show prompting user to choose again, if either 1 or 2 is not pressed,
    while not input_decoded.isnumeric():
        if input_decoded != '1' or input_decoded != '2':
            print("Invalid input. Please enter a number that is either 1 or 2")
        input_decoded = input("Would you like to check if your message can be decoded? \n" 
                              "Press 1 for yes to continue \n" 
                              "Press 2 for no, take me back to the topic menu \n") 
   
    if input_decoded == '1':   
        decoded_program(output_encoded)
        

def topic_3():
    """
    This function asks for user to copy the secret message to decode the it.
    """
    
    encoded_msg = input('Copy and paste to decode the message:\nÊë®¢Ë¢êñòç¢ûñ÷¢çðìñûçæ¢öêëõ¢òôñéôãï£')
    
    #will indefinitily ask user to copy and paste the secret msg until user does so correctly
    #an error message will show if user does not do so correctly
    while True:
        if encoded_msg != "Êë®¢Ë¢êñòç¢ûñ÷¢çðìñûçæ¢öêëõ¢òôñéôãï£":
            print("Are you sure you copied and pasted correctly? Try again")
            
            encoded_msg = input('Copy and paste to decode the message:\nÊë®¢Ë¢êñòç¢ûñ÷¢çðìñûçæ¢öêëõ¢òôñéôãï£')
        else:
            decoded_program(encoded_msg)
            break
            
def quit():
    """
    This function asks user if they want to end the program or not.
    """
    ask_quit = input("Are you sure you want to quit the program? Type q to quit. If not, press any key to continue \n")
    #will ask user if they want to quit the program, ends the while loop
    if ask_quit == 'q':
        return False
    return True