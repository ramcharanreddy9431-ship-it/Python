def find_nb(m):
    a = 0
    n = 1
    while m > 0:           #loop runs till sum of consecutive cubes is less than m
        m = m - n**3       #subtracts consecutive number cubes from m as you keep incrementing n later on
        a = a + 1          #keeps track of current iteration
        n = n + 1
    if m == 0:
        return a
    else:
        return -1          #returns -1 if its not a sum of consecutive volumes
        
