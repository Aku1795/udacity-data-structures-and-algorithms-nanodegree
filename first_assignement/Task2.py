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

def computeTimeSpentOnCall(calls):

    callingTimes = {}

    for c in calls:
        if callingTimes.get(c[0]) is None:
            callingTimes[c[0]] = int(c[3])
        if callingTimes.get(c[1]) is None:
            callingTimes[c[1]] = int(c[3])
        else:
            callingTimes[c[0]] += int(c[3])
            callingTimes[c[1]] += int(c[3])
    return callingTimes

def maxDurationNumber(callingTimes):
    maxCaller = max(callingTimes, key=callingTimes.get)
    maxDuration = callingTimes[maxCaller]
    return maxCaller, maxDuration

callingTimes = computeTimeSpentOnCall(calls)
maxCaller, maxDuration = maxDurationNumber(callingTimes)
answer = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(maxCaller, maxDuration)
print(answer)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

