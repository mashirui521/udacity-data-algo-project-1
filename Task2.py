"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def set_number_duration(number_time, number, time):
    number_time[number] = number_time.get(number, 0) + time

def task_2(calls):
    number_time = dict()
    for call in calls:
        set_number_duration(number_time, call[0], int(call[3]))
        set_number_duration(number_time, call[1], int(call[3]))

    max_phone = max(number_time, key=lambda i: number_time[i])
    max_duration = number_time[max_phone]
    return max_phone, max_duration
    
number, time = task_2(calls)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number, time))
