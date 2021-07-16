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

def getReceivers(data):
    """Returns set of numbers being at least once on the receiver end"""

    return set([row[1] for row in data ])

def getSender(data):
    """Returns set of numbers being at least once on the sender end"""


    return set([row[0] for row in data])

def getCallersWithoutTextings(calls, texts):
    """Returns the diffrence  between callers and texters"""

    callers = getSender(calls)
    texters = getSender(texts)

    return callers-texters

def getPotentialTeleMarketers(receivers, callersWithoutTexters):
    """Returns the intersection  between receivers and callersWithoutTexters"""

    return receivers&callersWithoutTexters

def finalPrint(potentialTelemarketers):

    print("These numbers could be telemarketers: ")
    potentialTelemarketers = sorted(list(potentialTelemarketers))
    for pt in potentialTelemarketers:
        print(pt)


def test():

    textReceivers = getReceivers(texts)
    callReceivers = getReceivers(calls)

    assert list(textReceivers) != []
    assert list(callReceivers) != []

def run():

    textReceivers = getReceivers(texts)
    callReceivers = getReceivers(calls)
    receivers = textReceivers.union(callReceivers)

    callersWithoutTexters = getCallersWithoutTextings(texts, calls)
    potentialTelemarketers = getPotentialTeleMarketers(receivers, callersWithoutTexters)

    finalPrint(potentialTelemarketers)


test()
run()
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

