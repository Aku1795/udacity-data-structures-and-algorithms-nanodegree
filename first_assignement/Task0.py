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
    
    

_str = "First record of texts, {incoming_number} texts {answering_number} at time {time}"
print(_str.format(incoming_number = texts[0][0], answering_number=texts[0][1], time=texts[0][2]))
n=len(calls)-1
_str = "Last record of calls, {incoming_number} calls {answering_number} at time {time}, lasting {during} seconds"
print(_str.format(incoming_number = calls[n][0], answering_number=calls[n][1], time=calls[n][2], during=calls[n][3]))

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

