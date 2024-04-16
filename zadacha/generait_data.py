import pandas as pd
from random import random 
import os

distance_between_events = []
sum = 0

for i in range(10000):
    x = random() * 10
    sum += x
    distance_between_events.append(x)  

time_of_event = [distance_between_events[0]]


for i in range(10000 - 1):
    time_of_event.append(time_of_event[i - 1] + distance_between_events[i])


data = pd.DataFrame(
    {
        'distance_between_events' : distance_between_events,
        'time_of_event' : time_of_event,
    }
                     )

path = 'data.csv'

try:
    open(path)
    os.remove(path)
    
    data.to_csv(path)

    print('Файл создан и заменен')
except:
     
    data.to_csv(path)
    print('Файл,создан и сохранен')   