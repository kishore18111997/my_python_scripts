#looping

for x in range(3,10, 2):
    x = (x+6)
    print(x)

l = [1,2,3,4,5,6,7]
print(l)
l.append(x)
l.insert (5, 3)
print(l)

f = open('E:\\DevOps office projects\\poc project\\ECG_PUT_000170.txt', 'r')

list=[]
for line in f:
    list.append([line.strip('\n')])

print(list)