"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def getPhoneNumbers(_list):
    """Get receiver and sender numbers and returns a list of all numbers in records"""
    phone_numbers = []
    for t in _list:
        phone_numbers.append(t[0])
        phone_numbers.append(t[1])

    return phone_numbers


with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)


def main():
    phone_numbers = getPhoneNumbers(texts) + getPhoneNumbers(calls)
    nb_phone_numbers = len(set(phone_numbers))
    answer = "There are {} different telephone numbers in the records.".format(
        nb_phone_numbers
    )
    print(answer)


main()


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
