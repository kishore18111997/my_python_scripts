f = open('E:\\DevOps office projects\\poc project\\ECG_PUT_000170.txt', 'r')

list=[]
for line in f:
    list.append([line.strip('\n')])

print(list)