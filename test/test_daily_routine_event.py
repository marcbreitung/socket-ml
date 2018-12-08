import unittest
from datetime import datetime
from utils.daily_routine_event import DailyRoutineEvent


class DailyRoutineItemTest(unittest.TestCase):
    def testConstructorWithAttributesSetsClassAttributes(self):
        item = DailyRoutineEvent('Name', 'Action', 'Workday', 'Holiday')
        self.assertEqual(item.name, 'Name')
        self.assertEqual(item.action, 'Action')
        self.assertEqual(item.workday, 'Workday')
        self.assertEqual(item.holiday, 'Holiday')

    def testGetTimedeltaWithWorkdayReturnsValuesForAWorkday(self):
        item = DailyRoutineEvent('Name', 'Action', 'Workday', 'Holiday')
        day = datetime(2018, 12, 6, 0, 0)
        self.assertEqual(item.get_timedelta(day), 'Workday')
