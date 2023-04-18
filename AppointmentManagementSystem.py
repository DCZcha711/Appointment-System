# AppointmentManagementSystem.py
# Yi-Chia Chu (chu.yi-c)
# 4/15/2023

from userClass import User
from appointmentDiaryClass import AppointmentDiary
from appointmentSystemClass import AppointmentSystem
from timeClass import Time
from dateClass import Date

""" Summary: A appointment management system that allows users to add, delete, and list users,
    add, delete, and list appointments, and check if an appointment conflicts with other appointments in the appointment diary. 
    The system will maintain users' appointments from now until December 31st, 2023
    
    Input: 1) one of the characters in 'adlscfprx' which each represents a different operation on the appointment system 
           2) input from user to indicate the operation to be performed

    Output: printed messages indicating the result of the operation
    
    """

def user_in_system(appointmentSystem, username):
    """Return True if the user is in the system, False otherwise."""
    if username in appointmentSystem.user_dict:
        return True
    print(f'User {username} does not exist in the system')
    return False


def is_valid_date_input(date_str):
    """Return True if the input date is valid, False otherwise."""
    year = date_str[0:4] # year of the input date
    month = date_str[5:7] # month of the input date
    day = date_str[8:10] # day of the input date

    # check if the date is in the correct format
    if (year.isnumeric() and month.isnumeric() and day.isnumeric() and date_str[4] == '-' and date_str[7] == '-') == False:
        print('Invalid date. Please enter a valid date.')
        return False
    # check if the date is valid
    date = Date(date_str) # create a Date object
    if not date.is_valid_date():
        return False
    return True


def is_valid_start_time_input(start_time_str):
    """Return True if the input start time is valid, False otherwise."""
    # check if the start time is in the correct format
    if (start_time_str[0:2].isnumeric() and start_time_str[3:5].isnumeric() and (start_time_str[6:8] == 'AM' or start_time_str[6:8] == 'PM') and start_time_str[2] == '-' and start_time_str[5] == '-') == False:
        print('Invalid start time. Please enter a valid time.')
        return False
    # check if the start time is valid
    start_time = Time(start_time_str) # create a Time object
    if not start_time.is_valid_start_time():
        return False
    return True


def is_valid_endtime(strat_time_str, end_time_str):
    """Return True if the input end time is valid, False otherwise."""
    # check if the end time is in the correct format
    if (end_time_str[0:2].isnumeric() and end_time_str[3:5].isnumeric() and (end_time_str[6:8] == 'AM' or end_time_str[6:8] == 'PM') and end_time_str[2] == '-' and end_time_str[5] == '-') == False:
        print('Invalid end time. Please enter a valid time.')
        return False
    # check if the end time is valid
    end_time = Time(end_time_str) # create a Time object
    if not end_time.is_valid_end_time(strat_time_str):
        return False
    return True


def is_valid_input(appointmentSystem):
    """Return True if the input is valid, False otherwise."""
    args = {} # dictionary to store the input arguments
    username = input('Enter username: ') # username of the user
    if not user_in_system(appointmentSystem, username):
        return False, {}
    date_str = input('Enter date in format YYYY-MM-DD: ')
    if not is_valid_date_input(date_str):
        return False, {}
    start_time_str = input('Enter start time in format HH-MM-AM or HH-MM-PM: ')
    if not is_valid_start_time_input(start_time_str):
        return False, {}
    end_time_str = input('Enter end time in format HH-MM-AM or HH-MM-PM: ')
    if not is_valid_endtime(start_time_str, end_time_str):
        return False, {}
    args['username'] = username
    args['date_str'] = date_str
    args['start_time_str'] = start_time_str
    args['end_time_str'] = end_time_str
    return True, args

if __name__ == '__main__':
        appointmentSystem = AppointmentSystem() # create an instance of AppointmentSystem
        # check whether the input for menu choice is valid
        while True:
            while True:
                # display the menu options
                print()
                print('Welcome to Appointment Management System! What would you like to do?\n[a] Add new user\n[d] Delete an existing user\n[l] List existing users\n[s] Schedule an appointment\
                      \n[c] Cancel an appointment\n[f] Check for appointment on certain date and time\n[p] Retrieve purpose of an appointment\n[r] Reschedule an existing appointment\
                      \n[x] Exit the system')
                choice = input('Enter choice: ') # get input option
                print()
                
                # check unexpected/invalid inputs like a integer for menu choice
                if choice not in 'adlscfprx':
                    print('Invalid input. Please enter a choice from the menu.')
                else:
                    break
            
            if choice == 'x':
                # terminates the program if entering a choice of [x]
                print('Goodbye!')
                break
            elif choice == 'a':
                # add new user
                username = input('Enter username: ') # get username     
                appointmentSystem.add_user(username)              
            elif choice == 'd':
                # remove the user from the system, delete all entries in its diary, and any other relevant user specific data
                username = input('Enter username: ') # get username
                appointmentSystem.delete_user(username)
            elif choice == 'l':
                # print a list of all the usernames currently holding appointment diaries in the system
                appointmentSystem.list_user()
            elif choice == 's':
                # schedule an appointment
                is_valid, args = is_valid_input(appointmentSystem)
                if not is_valid:
                    continue
                purpose = input('Enter purpose: ') # get purpose
                appointmentSystem.scheduleAppointment(args['username'], 
                                                      args['date_str'], 
                                                      args['start_time_str'], 
                                                      args['end_time_str'], 
                                                      purpose)
            elif choice == 'c':
                # cancel an appointment
                is_valid, args = is_valid_input(appointmentSystem)
                if not is_valid:
                    continue
                appointmentSystem.cancelAppointment(args['username'], 
                                                      args['date_str'], 
                                                      args['start_time_str'], 
                                                      args['end_time_str'])
            elif choice == 'f':
                # check for appointment on certain date and time
                is_valid, args = is_valid_input(appointmentSystem)
                if not is_valid:
                    continue
                appointmentSystem.checkAppointment(args['username'], 
                                                      args['date_str'], 
                                                      args['start_time_str'], 
                                                      args['end_time_str'])
            elif choice == 'p':
                # retrieve purpose of an appointment
                is_valid, args = is_valid_input(appointmentSystem)
                if not is_valid:
                    continue
                appointmentSystem.retrievePurpose(args['username'], 
                                                  args['date_str'], 
                                                  args['start_time_str'], 
                                                  args['end_time_str'])
            elif choice == 'r':
                # reschedule an existing appointment
                is_valid, args = is_valid_input(appointmentSystem)
                if not is_valid:
                    continue
                username = args['username'] # get username
                if not is_valid:
                    continue
                if appointmentSystem.checkAppointment(args['username'], 
                                                   args['date_str'], 
                                                   args['start_time_str'], 
                                                   args['end_time_str']):
                    continue
                appointmentSystem.cancelAppointment(args['username'], 
                                                   args['date_str'], 
                                                   args['start_time_str'], 
                                                   args['end_time_str'])
                print('Enter new appointment information')
                if not is_valid:
                    continue
                date_str = input('Enter date in format YYYY-MM-DD: ')
                if not is_valid_date_input(date_str):
                    continue
                start_time_str = input('Enter start time in format HH-MM-AM or HH-MM-PM: ')
                if not is_valid_start_time_input(start_time_str):
                    continue
                end_time_str = input('Enter end time in format HH-MM-AM or HH-MM-PM: ')
                if not is_valid_endtime(start_time_str, end_time_str):
                    continue
                new_purpose = input('Enter purpose: ')
                appointmentSystem.scheduleAppointment(username, 
                                                      date_str, 
                                                      start_time_str, 
                                                      end_time_str, 
                                                      new_purpose)