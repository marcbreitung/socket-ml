from datetime import timedelta
from datetime import datetime


class DailyRoutineData:
    def __init__(self, period=10, start='2018-01-01'):
        self.period = period
        self.start = start
        self.daily_routine_events = []
        self.data = []

    def add_daily_routine_event(self, daily_routine_event):
        self.daily_routine_events.append(daily_routine_event)

    def get_data(self):
        start_day = datetime.strptime(self.start, '%Y-%m-%d')
        for day in range(self.period):
            today = start_day + timedelta(days=day)
            for item in self.daily_routine_events:
                if item.get_timedelta(today) is not None:
                    date = today + item.get_timedelta(today)
                    self.data.append({
                        'day': today.weekday(),
                        'name': item.name,
                        'action': item.action,
                        'date': date.strftime("%Y-%m-%d %H:%M:%S"),
                        'timestamp': int(date.timestamp())
                    })
        return self.data
