# appointmentDiaryClass.py
# Yi-Chia Chu (chu.yi-c)
# 4/15/2023
from timeClass import Time

class AppointmentDiary(object):
    """
    a list of all the appointments that a given user has scheduled.
    
    Attributes
        appointment_dict : {date: [appointment1, appointment2, appointment3]}
    """
    
    def __init__(self):
        """ Returns a AppointmentDiary representation of the user name encoded in user.

        """
        self.appointment_dict = {} # dictionary of Appointments

    
    def add_appointment(self, date, start_time, end_time, purpose):
        """ Adds a new appointment to the appointment diary."""
        # check if date exists in user's appointment diary
        if date not in self.appointment_dict:
            self.appointment_dict[date] = []
        self.appointment_dict[date].append([start_time, end_time, purpose])
        self.appointment_dict[date].sort()
        print(f'Appointment on {date} from {start_time} to {end_time} added successfully.')

    
    def get_appointment_index(self, date, start_time, end_time):
        """ Returns the index of the appointment in the appointment list."""
        for idx in range(len(self.appointment_dict[date])):
            if start_time == self.appointment_dict[date][idx][0] and end_time == self.appointment_dict[date][idx][1]:
                return idx
        return -1


    def delete_appointment(self, date, start_time, end_time):
        """ Deletes an appointment from the appointment diary."""
        if date not in self.appointment_dict:
            print(f'No appointment on {date}.')
            return
        appointment_index = self.get_appointment_index(date, start_time, end_time) # index of the appointment in the appointment list
        if appointment_index == -1:
            print(f'No appointment on {date} from {start_time} to {end_time}.')
            return
        del self.appointment_dict[date][appointment_index]
        if len(self.appointment_dict[date]) == 0:
            del self.appointment_dict[date]
        print(f'Appointment on {date} from {start_time} to {end_time} deleted successfully.')    


    def check_appointment(self, date, start_time, end_time):
        """ Checks if an appointment exists in the appointment diary."""
        if date not in self.appointment_dict:
            print(f'No appointment on {date}.')
            return False
        #check_time = Time(check_time)
        appointment_index = self.get_appointment_index(date, start_time, end_time)
        if appointment_index == -1:
            print(f'No appointment on {date} from {start_time} to {end_time}.')
            return False
        print(f'Appointment on {date} from {start_time} to {end_time} found.')  
        return True


    def retrieve_purpose(self, date, start_time, end_time):
        """ Retrieves the purpose of an appointment."""
        if date not in self.appointment_dict:
            print(f'No appointment on {date}.')
            return
        appointment_index = self.get_appointment_index(date, start_time, end_time)
        if appointment_index == -1:
            print(f'No appointment on {date} from {start_time} to {end_time}.')
            return
        print(f'Purpose of the appointment: {self.appointment_dict[date][appointment_index][2]}.')    
