# Assignment

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.
Your task is to determine the following:
1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773


## Approach
- **Initialization**: A dynamic programming (attend_table) table,  attend_table of size (N+1) * 4 is initialized to store the number of ways to attend classes with up to 3 consecutive absences.
- **Base Case**: The initial state is attend_table[0][0] = 1, On day 0, with 0 consecutive absences, only 1 way
- **Table Filling**: For each day i from 1 to N, the table is filled by considering:
    Attending class ( j = 0 ), adding all ways from the previous day.
    Missing class ( j > 0 ), switching from j-1 consecutive absences from the previous day.
- **Calculation**: The total number of valid sequences and the number of sequences missing the graduation ceremony are calculated from the attend_table table.
- **Result**: The result is returned as a fraction of sequences missing the graduation to the total valid sequences.

## Time and Space Complexity
- **Time Complexity**: O(N) - It iterates through N days with the same amount of work .
- **Space Complexity**: O(N) -  Amount of memory needed for the attend_table table grows in proportion to the number of days, N.
