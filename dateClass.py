# dataClass.py
# Yi-Chia Chu (chu.yi-c)
# 4/15/2023

from datetime import date

class Date(object):
    """
    Represents a date.
    
    Attributes
        year : year of the date [int]  
        month : month of the date [int]
        day : day of the date [int]
    """
    
    def __init__(self,date_str):
        """ Returns a Date representation of the date encoded in date.
        
        PreC: s is a date string of the form 'YYYY-MM-DD'.
        """
        # self.year, self.month, self.day = date_str.split('-')
        v = date_str.split('-')
        self.year = int(v[0])
        self.month = int(v[1])
        self.day = int(v[2])
    
    def __lt__(self, other_date):
        """Return True if self < other_date, False otherwise."""
        if self.year < other_date.year:
            return True
        if self.year == other_date.year and self.month < other_date.month:
            return True
        if self.year == other_date.year and self.month == other_date.month and self.day < other_date.day:
            return True
        return False
    
    def __gt__(self, other_date):
        """Return True if self > other_date, False otherwise."""
        if self.year > other_date.year:
            return True
        if self.year == other_date.year and self.month > other_date.month:
            return True
        if self.year == other_date.year and self.month == other_date.month and self.day > other_date.day:
            return True
        return False

    def is_leap_year(self):
        """ Returns True if y is a leap year. False otherwise
    
        PreC: y is a positive integer
        """
        y = self.year
        return ((y%100>0) and y%4==0) or ((y%100==0) and (y%400==0))
    
    def is_valid_date(self):
        """Return True if the input date is valid, False otherwise."""
        today = date.today()
        month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # the number of days in each month
        # check if the date is valid
        
        # check if the date is in the past
        if self < today:
            print('Invalid date. Please enter a valid date that is not in the past.')
            return False
        # check if the date is after 2023-12-31
        if self > Date('2023-12-31'):
            print('Invalid date. Please enter a valid date that is not after 2023-12-31.')
            return False
        # # check if the year is valid
        # if self.year < today_year:
        # if self.year <= 0 or self.year > 9999:
        #     print('Invalid year. Please enter a valid year.')
        #     return False
        # # check if the month is valid
        # if self.month <= 0 or self.month > 12:
        #     print('Invalid month. Please enter a valid month.')
        #     return False
        # # check if the day is valid
        # if self.is_leap_year():
        #     month_day[1] = 29
        # if self.day > month_day[self.month - 1] or self.day <= 0:
        #     print('Invalid day. Please enter a valid day.')
        #     return False
        return True
