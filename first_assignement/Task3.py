"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

# constants
BENGALORE_CODE = "(080)"


def containsCode(call, code):
    if code in call:
        return True
    return False


def getCallsFrom(calls, code):
    """Keeping only land line calls from Bengalore"""

    return [c for c in calls if containsCode(c[0], code)]


def extractAreaCode(number):
    """Given a called number extract the area code"""
    if number[:3] == "140":
        return "140"
    if number[0] == "(":
        return number.split(")")[0] + ")"
    if number[0] in ["7", "8", "9"]:
        return number[:4]


def computeCallsoPerCodes(callsFrom):
    """For each area code reached from Bengalore compute total number of calls"""
    nbCallsPerCode = {}

    for c in callsFrom:
        code = extractAreaCode(c[1])
        if nbCallsPerCode.get(code) is None:
            nbCallsPerCode[code] = 1
        else:
            nbCallsPerCode[code] += 1
    return nbCallsPerCode


def orderedAreaCodes(nbCallsPerCode):
    """Returns in lexicographic order the area codes reached"""

    return sorted(nbCallsPerCode.keys())


def printPartA(nbCallsPerCode):
    area_codes = orderedAreaCodes(nbCallsPerCode)
    print("The numbers called by people in Bangalore have codes:")
    for c in area_codes:
        print(c)


def printPartB(nbCallsPerCode):

    landlineCalls = sum([nbCallsPerCode[c] for c in nbCallsPerCode if c[0] == "("])
    landlinePct = round(nbCallsPerCode["(080)"] * 100.0 / (landlineCalls), 2)
    answer = "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore".format(
        landlinePct
    )

    print(answer)


def test():
    assert containsCode("(080)575757", BENGALORE_CODE) == True
    assert len(getCallsFrom(calls, BENGALORE_CODE)) != 0
    assert extractAreaCode("(080)") == "(080)"
    assert extractAreaCode("(08009)") == "(08009)"
    assert extractAreaCode("98009 000949") == "9800"
    assert extractAreaCode("140000949") == "140"
    nbCallsPerCode = computeCallsoPerCodes(getCallsFrom(calls, BENGALORE_CODE))
    assert len(orderedAreaCodes(nbCallsPerCode)) != 0

    print()
    print("All test succeeded!")


def run():
    nbCallsPerCode = computeCallsoPerCodes(getCallsFrom(calls, BENGALORE_CODE))
    printPartA(nbCallsPerCode)
    printPartB(nbCallsPerCode)


test()
run()

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
