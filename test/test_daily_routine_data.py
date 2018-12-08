import unittest
from datetime import timedelta
from utils.daily_routine_data import DailyRoutineData
from utils.daily_routine_event import DailyRoutineEvent


class DailyRoutineDataTest(unittest.TestCase):
    def test_constructor_with_attributes_sets_class_attributes(self):
        data = DailyRoutineData(period=10, start='2018-01-01')
        self.assertEqual(data.period, 10)
        self.assertEqual(data.start, '2018-01-01')

    def test_add_daily_routine_event_adds_item_to_attribute_daily_routine_events(self):
        data = DailyRoutineData(period=10, start='2018-01-01')
        event1 = DailyRoutineEvent('wake up', 'on', timedelta(hours=7, minutes=30), timedelta(hours=10))
        event2 = DailyRoutineEvent('go to work', 'off', timedelta(hours=8), None)
        data.add_daily_routine_event(event1)
        data.add_daily_routine_event(event2)
        self.assertEqual(data.daily_routine_events[0], event1)

    def test_get_data_returns_list_with_test_data(self):
        data = DailyRoutineData(period=7, start='2018-01-01')
        event1 = DailyRoutineEvent('wake up', 'on', timedelta(hours=7, minutes=30), timedelta(hours=10))
        event2 = DailyRoutineEvent('go to work', 'off', timedelta(hours=8), None)
        data.add_daily_routine_event(event1)
        data.add_daily_routine_event(event2)

        expected = [
            {'day': 0, 'name': 'wake up', 'action': 'on', 'date': '2018-01-01 07:30:00', 'timestamp': 1514788200},
            {'day': 0, 'name': 'go to work', 'action': 'off', 'date': '2018-01-01 08:00:00', 'timestamp': 1514790000},
            {'day': 1, 'name': 'wake up', 'action': 'on', 'date': '2018-01-02 07:30:00', 'timestamp': 1514874600},
            {'day': 1, 'name': 'go to work', 'action': 'off', 'date': '2018-01-02 08:00:00', 'timestamp': 1514876400},
            {'day': 2, 'name': 'wake up', 'action': 'on', 'date': '2018-01-03 07:30:00', 'timestamp': 1514961000},
            {'day': 2, 'name': 'go to work', 'action': 'off', 'date': '2018-01-03 08:00:00', 'timestamp': 1514962800},
            {'day': 3, 'name': 'wake up', 'action': 'on', 'date': '2018-01-04 07:30:00', 'timestamp': 1515047400},
            {'day': 3, 'name': 'go to work', 'action': 'off', 'date': '2018-01-04 08:00:00', 'timestamp': 1515049200},
            {'day': 4, 'name': 'wake up', 'action': 'on', 'date': '2018-01-05 07:30:00', 'timestamp': 1515133800},
            {'day': 4, 'name': 'go to work', 'action': 'off', 'date': '2018-01-05 08:00:00', 'timestamp': 1515135600},
            {'day': 5, 'name': 'wake up', 'action': 'on', 'date': '2018-01-06 10:00:00', 'timestamp': 1515229200},
            {'day': 6, 'name': 'wake up', 'action': 'on', 'date': '2018-01-07 10:00:00', 'timestamp': 1515315600}]

        self.assertEqual(data.get_data(), expected)
