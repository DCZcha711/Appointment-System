# userClass.py
# Yi-Chia Chu (chu.yi-c)
# 4/15/2023


# Create a user class to represent each user of the system
class User(object):
    """
    Representing each user of the system
    
    Attributes
       u : user name
       ap : AppointmentDiary, representing each user of the system
    """
    
    def __init__(self, user_name, appointment_diary):
        """ Returns a User representation of the user name encoded in user.
        
        PreC: .
        """
        self.user_name = user_name
        self.appointment_diary = appointment_diary

    # # add a new user to the system
    # def addUser(self, u_name):
    #     """The system asks for a new username, adds the user to the system, 
    #     and creates a new appointment diary for the specified user"""

    #     # check if the user already exists in the system
    #     # print an error message and go back to the welcome screen
    #     if u_name in self.appointment_diary:
    #         print(f"User {u_name} already exists")
    #     # If adding was successful
    #     # print a message indicating that and go back to the welcome screen
    #     else:
    #         self.appointment_diary.append(u)
    #         print(f"User {u_name} added successfully")

    
    # # [d] Delete an existing user
    # def deleteUser(self, u):
    #     """The system asks for the username to be deleted"""
    #     # check if the user exists
    #     # remove the user from the system, delete all entries in its diary, and any other relevant user specific data
    #     # print a success message and go back to the welcome screen
    #     if u in self.appointment_diary:
    #         self.appointment_diary.remove(u)
    #         print("User deleted successfully")
    #     # If the user was not found
    #     # print an error message and return to the welcome screen
    #     else:
    #         print("User not found")

    # # [l] List existing users
    # def listUser(self):
    #     """Print a list of all the usernames currently holding appointment diaries in the system."""
    #     print(self.appointment_diary)

        

