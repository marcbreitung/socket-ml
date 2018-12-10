# The Machine Learning Socket


## Utils 
The classes DailyRoutineEvent and DailyRoutineData generate some test data for a machine learning socket.
  
  
### class DailyRoutineEvent
Defines an event in the life of an ordinary socket, usually these events are turn off the socket or turn it on. But you can define some additional settings.


#### DailyRoutineEvent(name, action, workday, holiday)

* **name:** a string with the name for this event
* **action:** a string with the action for this event ('on', or 'off')
* **workday:** a timedelta when the event should occur on workday 
* **holiday:** a timedelta when the event should occur on holiday 

To generate a more realistic data, you should add some randomness with [randrange()](https://docs.python.org/3.7/library/random.html?highlight=randrange#random.randrange)

````python
from random import randrange
from datetime import timedelta
from utils.daily_routine_event import DailyRoutineEvent

event = DailyRoutineEvent('wake up', 'on', timedelta(hours=7, minutes=30 + randrange(-10, 10)), timedelta(hours=10, minutes=randrange(-30, 30)))
````

#### get_timedelta(day)

* **day:** datetime object

Returns the timedelta for a workday if the given day is a workday or a the timedelta for a holiday otherwise


### class DailyRoutineData
Builds a python list with the generated events for a given period of days.

#### DailyRoutineData(period=10, start='2018-01-01')

* **period:** number of days, default value is 10
* **start:** the start date for the test data, default value is '2018-01-01'


#### add_daily_routine_event(daily_routine_event)

Adds a DailyRoutineEvent to the DailyRoutineData.

* **daily_routine_event:** a DailyRoutineEvent object


#### get_data()

Returns the list with the generated test data.


## JupyterLab with Docker
```bash
docker run --rm -p 10000:8888 -v "$PWD":/home/jovyan/work jupyter/scipy-notebook:latest start.sh jupyter lab
```

Open the ```localhost:10000/?token=TOKEN``` in the browser