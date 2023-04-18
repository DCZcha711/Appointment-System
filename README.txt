# README.txt
# Yi-Chia Chu (chu.yi-c)
# 4/15/2023

a) Include a quick summary of how you run your program.

    Summary: A appointment management system that allows users to add, delete, and list users,
    add, delete, and list appointments, and check if an appointment conflicts with other appointments in the appointment diary. 
    The system will maintain users' appointments from now until December 31st, 2023
    
    Input: 1) one of the characters in 'adlscfprx' which each represents a different operation on the appointment system 
           2) input from user to indicate the operation to be performed

    Output: printed messages indicating the result of the operation

    When run AppointmentManagementSystem.py, there will be a menu pop up in the terminal.
    'Welcome to Appointment Management System! What would you like to do?
    [a] Add new user
    [d] Delete an existing user
    [l] List existing users
    [s] Schedule an appointment                      
    [c] Cancel an appointment
    [f] Check for appointment on certain date and time
    [p] Retrieve purpose of an appointment
    [r] Reschedule an existing appointment                      
    [x] Exit the system
    Enter choice:'

    The program will then operate according to the user's input.
    If the user enters an invalid option, the program will print out an error message.
    If the user enters a valid option, the program will ask for more input regarding the option a user entered.

    In the operation process, i fin any steps the given input from the user is invalid, 
    the program will print out an error message and return to the option menu.
    Otherwise, when the operation is done, the program will print out a message indicating the operation is done and then return to the option menu.

    The program will repeat until the user explicitly terminates the program by entering a choice of [x].

b) If any of the functionality in your programs is not working, include what is the issue in your
opinion and how would you fix it if you had more time?
    
    After running the programs several times, I think my programs are working correctly.
