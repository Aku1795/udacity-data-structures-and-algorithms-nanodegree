#Complexity analysis


Common to all tasks is the number of operations needed to read in the csv files “text.csv” and “calls.csv” into python lists. This operation is O(2).

## Task 0

After reading in the files 5 simple operations are performed so the worst case scenario is to get a O(5).

## Task 1
The worst case scenario is a O(4n+2) and below is the detailed explanation:

    ⁃	Getting all the numbers in both records has a number of operations equal to O(4n) (O(2n) per record cause we need to iterate through all rows and excecute 2 operation per rows)

    ⁃	Getting the length of the list is a O(1) operation

    ⁃	Printing the message is a O(1).
## Task 2
The worst case scenario is a O(2n+1) and below is the detailed explanation:

    ⁃	O(n) for getting the calling times per number

    ⁃	O(n)  for getting the maximum duration

    ⁃	O(1) for printing

## Task 3

The worst case scenario is a O(4n + nlogn) for part A and below is the detailed explanation:

    - O(n) for computing the number of calls per number

    - O(nlogn) for sorting the numbers in lexical order

    - O(n) for printing the numbers

    - O(2n) for computing the percentage of landline calls


## Task 4

The worst case scenario is a O(n^2 + nlogn + 12n) and below is the detailed explanation:

    ⁃	O(4n) for generating the textReceivers and callReceivers sets

    ⁃	O(4n) for generating the receivers set (union operation)

    ⁃	O(3n) for generating the callersWithoutTexters (difference operation)

    ⁃	O(n^2) for the final list (intersection operation)

    -   O(nlogn) for sorting the list

    ⁃	O(n) for printing

