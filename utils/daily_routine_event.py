class DailyRoutineEvent:
    def __init__(self, name, action, workday, holiday):
        self.name = name
        self.action = action
        self.workday = workday
        self.holiday = holiday

    def get_timedelta(self, day):
        if day.weekday() < 5:
            return self.workday
        else:
            return self.holiday
