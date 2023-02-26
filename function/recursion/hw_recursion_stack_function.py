def decreaseInt(n):
    print(n)
    n -= 1
    if n != 0:
        
        return decreaseInt(n)
    else:
        return n

    ########################
    # HW3: draw the memory diagram


n = 10
n = decreaseInt(n)

print(n)
