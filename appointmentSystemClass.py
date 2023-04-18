# appointmentSystemClass.py
# Yi-Chia Chu (chu.yi-c)
# 4/15/2023
from dateClass import Date
from timeClass import Time
from userClass import User
from appointmentDiaryClass import AppointmentDiary
from appointmentClass import Appointment


class AppointmentSystem(object):
    """
    Represents an appointment system.
    
    Attributes
        user_dict : {USER: AppointmentDiary }
    """
    
    def __init__(self):
        """ Returns an AppointmentSystem representation of the appointment system."""
        self.user_dict = dict() # {USER: AppointmentDiary }


    def add_user(self, username):
        """Add a new user to the system."""
        if username in self.user_dict:
            print(f'User {username} already exists in the system.')
        else:
            self.user_dict[username] = User(username, AppointmentDiary())
            print('User added successfully.')

    
    def delete_user(self, username):
        """Delete a user from the system."""
        if username not in self.user_dict:
            print(f'User {username} does not exist in the system')
        else:
            del self.user_dict[username]
            print(f'User {username} deleted successfully.')

    
    def list_user(self):
        """List all users in the system."""
        if len(self.user_dict) == 0:
            print('No users in the system')
        for user in self.user_dict:
            print(user)

    
    def is_conflict(self, username, date, start_time, end_time):
        """Checks if an appointment conflicts with other appointments in the appointment diary."""
        appointment_dict = self.user_dict[username].appointment_diary.appointment_dict # {date: [appointment1, appointment2, appointment3]}
        # check if date exists in user's appointment diary
        if date not in appointment_dict:
            return False
        appointment_on_date = appointment_dict[date] # [appointment1, appointment2, appointment3]
        start_time = Time(start_time) # create a starttime Time object
        end_time = Time(end_time) # create a endtime Time object

        if end_time < Time(appointment_on_date[0][0]):
            return False
        if start_time > Time(appointment_on_date[-1][1]):
            return False
        num_appointment = len(appointment_on_date) # number of appointments on the date
        if num_appointment > 1:
            for idx in range(0, num_appointment - 1):
                curr_appointment = appointment_on_date[idx] # [start_time, end_time, purpose] of current appointment
                next_appointment = appointment_on_date[idx+1] # [start_time, end_time, purpose] of next appointment
                if start_time > Time(curr_appointment[1]) and end_time < Time(next_appointment[0]):
                    return False
            return True
        return True
        

    def scheduleAppointment(self, username, date, start_time, end_time, purpose):
        """Add the appointment as long as it does not conflict with an existing appointment.
        Ask for username , date , time , and purpose."""

        # In case of conflict, print appropriate error message and go back to the welcome screen.
        if self.is_conflict(username, date, start_time, end_time):
            print('Appointment is conflict with an existing appointment')
            return
        self.user_dict[username].appointment_diary.add_appointment(date, start_time, end_time, purpose)


    def cancelAppointment(self, username, date, start_time, end_time):
        """Delete the appointment if it exists.
        Ask for username , date , time"""    
        self.user_dict[username].appointment_diary.delete_appointment(date, start_time, end_time)

    
    def checkAppointment(self, username, date, start_time, end_time):
        """Check if the appointment exists.
        Ask for username , date , time"""
        self.user_dict[username].appointment_diary.check_appointment(date, start_time, end_time)

    
    def retrievePurpose(self, username, date, start_time, end_time):
        """Retrieve the purpose of the appointment.
        Ask for username , date , time"""
        self.user_dict[username].appointment_diary.retrieve_purpose(date, start_time, end_time)