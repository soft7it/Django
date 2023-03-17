# ##############
_lock = False  # _private

# HW1: raise exception When lock found .... correct state
# HW2: make custom LockError class
def loadCount():
    global _lock
    if _lock == False:
        file = open('data.txt', 'r')
        count = int(file.read())
        file.close()
        _lock = True
        return count
    else:
        return None
    
def saveCount(count):
    global _lock
    if _lock == True:
        file = open('data.txt', 'w')
        file.write( str(count) )
        file.close()
        _lock = False
    else:
        print('Error!!! breach found!')        