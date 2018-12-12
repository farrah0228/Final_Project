# Final_Project
My Final Project for COGS18

This program lets a user pick a desired topic from the menu below by pressing numbers 1-4
1. Password Generation
2. Encrypt a message
3. Decrypt a seccret message
4. Quit program 

For topic 1, password generation, the program will first prompt user to input a desired length and then a desired amount of passwords. From a given string of characters, it randomly chooses these characters to create the password. The program will print out the desired length and amount of passwords the user wants. This portion of the program uses the function called password_func(length, amount), where the user input is passed through this function.

For topic 2, encrypt a message, the program will prompt user to input a desired message they would like to encrypt. After given the encypted message, the user will have the option to either see their encrypted message decrypted or return back to the topic menu. This portion of the program uses the function encoded_program(input_message) and decoded_program(input_secret) depending if the user would like to decrypt their encrypted message.

For topic 3, decrypt a secret message, the program will prompt user to copy and paste a secret encypted message and after, the decoded message will appear. If the message was copied and pasted incorrectly, the program will prompt user again to enter it correctly. This portion of the program uses the function decoded_program(input_secret) to decode the message.

For topic 4, quit program, it will ask if user really wants to quit, then the program will prompt user to press q to quit. This portion of the program uses the function quit() to end the program.
