# real data  consumer
from real import getData

localData = [10,20,30]
data = getData()

sum = localData[0] + localData[1] + localData[2]

answer = input('should include external data (y/n) ? ')

if answer == 'y':
    sum += data[0]

print(sum)    
