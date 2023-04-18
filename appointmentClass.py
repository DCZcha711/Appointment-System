# appointment.py
# Yi-Chia Chu (chu.yi-c)
# 4/15/2023


class Appointment():
    """ Represents an appointment.
        
        Attributes
            date : date of the appointment [Date]
            start_time : start time of the appointment [Time]
            end_time : end time of the appointment [Time]
            purpose : purpose of the appointment [string]
    """
    def __init__(self, date, start_time, end_time, purpose):
        """ Returns an Appointment representation of the appointment encoded in time."""
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.purpose = purpose
    
    def __lt__(self, another_appointment):
        pass

    def __gt__(self, another_appointment):
        pass
