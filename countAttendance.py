def count_attendance_sequences(N):
    # If its 0 days, there's no way to miss graduation
    if N == 0:
        return "0/1"

    # Initialize a table (attend_table) with dimensions (N+1) x 4 filled with zeros
    attend_table = [[0] * 4 for _ in range(N+1)]

    # Initial state: On day 0, with 0 consecutive absences, only 1 way
    attend_table[0][0] = 1

    # Fill the table
    for i in range(1, N+1):
        for j in range(4):
            
            if j == 0:
                # If attending class today, sum all ways from the previous day even its absencent
                attend_table[i][j] = sum(attend_table[i-1])
            else:
                # If missing class today, the previous day must have j-1 absences
                attend_table[i][j] = attend_table[i-1][j-1]

    # Calculate total valid sequences of length N
    total_ways = sum(attend_table[N])
    # Calculate sequences of length N where the last day is missed
    miss_graduation_ways = sum(attend_table[N][1:])
    
    return f"{miss_graduation_ways}/{total_ways}"

# Test cases
print(count_attendance_sequences(5))  # Expected: 14/29
print(count_attendance_sequences(10))  # Expected: 372/773

print(count_attendance_sequences(7))  # Expected: 52/108
print(count_attendance_sequences(3))  # Expected: 4/8

