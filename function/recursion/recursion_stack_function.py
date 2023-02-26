def increaseInt(n):
    n += 1
    if n !=  10:
        return increaseInt(n)
    else:
        return n
    
    ########################
    # HW3: draw the memory diagram

n = 1
n = increaseInt(n)

print(n)