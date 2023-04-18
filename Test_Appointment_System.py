from appointmentClass import Appointment
from appointmentDiaryClass import AppointmentDiary
from appointmentSystemClass import AppointmentSystem
from AppointmentManagementSystem import is_valid_date
from AppointmentManagementSystem import user_in_system

import unittest


class TestAppointmentDiary(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

class TestAppointmentManagementSystem(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_is_valid_date(self):
        date = '1233-12-12'
        self.assertTrue(is_valid_date(date))
        date = '1edefef'
        self.assertFalse(is_valid_date(date))
        date = '1233-'
        self.assertFalse(is_valid_date(date))
        date = '0000-00-00'
        self.assertFalse(is_valid_date(date))
        date = '9999-12-12'
        self.assertTrue(is_valid_date(date))
        date = '10000-12-12'
        self.assertFalse(is_valid_date(date))
    
    def test_user_in_system(self):
        # Integration test
        appointmentSystem = AppointmentSystem()
        appointmentSystem.add_user('user1')
        self.assertTrue(user_in_system(appointmentSystem,'user1'))

        appointmentSystem = AppointmentSystem()
        appointmentSystem.add_user('user2')
        self.assertFalse(user_in_system(appointmentSystem,'user1'))
        
    


if __name__ == '__main__':
    unittest.main()