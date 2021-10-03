"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
import collections

def get_numbers(content):
    return [content[0], content[1]]

def task_1(texts, calls):
    phone_numbers = set()
    for element in texts+calls:
        phone_numbers.update(get_numbers(element))
    return phone_numbers
    
phone_numbers = task_1(texts, calls)
print("There are {} different telephone numbers in the records.".format(len(phone_numbers)))
