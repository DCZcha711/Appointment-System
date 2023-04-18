# timeClass.py
# Yi-Chia Chu (chu.yi-c)
# 4/15/2023

class Time(object):
    """
    Represents a time.
    
    Attributes
        hour : hour of the time [int]
        minute : minute of the time [int]
        ampm : am or pm of the time [string]
    """
    
    def __init__(self,time_str):
        """ Returns a Time representation of the time encoded in time.
        
        PreC: time is a time string of the form 'HH-MM-AM' or 'HH-MM-PM.
        """
        #self.hour, self.minute, self.apm = time_str.split('-')
        v = time_str.split('-')
        self.hour = int(v[0])
        self.minute = int(v[1])
        self.ampm = v[2]
        if self.ampm == 'PM' and self.hour != 12:
            self.hour += 12
            if self.hour == 24:
                self.hour = 0
        if self.hour == 12 and self.ampm == 'AM':
            self.hour = 0

    
    def __lt__(self, other_time):
        """Return True if self < other_time, False otherwise."""
        if self.hour < other_time.hour:
            return True
        if self.hour == other_time.hour and self.minute < other_time.minute:
            return True
        return False

    def __gt__(self, other_time):
        """Return True if self > other_time, False otherwise."""
        if self.hour > other_time.hour:
            return True
        if self.hour == other_time.hour and self.minute > other_time.minute:
            return True
        return False

    def __eq__(self, other_time):
        """Return True if self == other_time, False otherwise."""
        return self.hour == other_time.hour and self.minute == other_time.minute


    def is_valid_start_time(self):
        """Return True if the input time is valid, False otherwise."""
        
        # check if the hour is valid (0-23)
        if self.hour < 0 or self.hour >= 24:
            print('Invalid start time hour. Please enter a valid hour.')
            return False
        # check if the minute is valid (0-59)
        if self.minute < 0 or self.minute > 59:
            print('Invalid start time minute. Please enter a valid minute.')
            return False
        return True
    
    def is_valid_end_time(self, start_time_str):
        """Return True if the input time is valid, False otherwise."""
        start_time = Time(start_time_str)
        # check if the end time is valid
        
        # check if the hour is valid (0-23)
        if self.hour < 0 or self.hour >= 24:
            print('Invalid end time hour. Please enter a valid hour.')
            return False
        # check if the minute is valid (0-59)
        if self.minute < 0 or self.minute > 59:
            print('Invalid end minute. Please enter a valid minute.')
            return False
        if self.hour < start_time.hour:
            print('Invalid end time. Please enter a valid time.')
            return False
        if self.hour == start_time.hour and self.minute <= start_time.minute:
            print('Invalid end time. Please enter a valid time.')
            return False
        return True