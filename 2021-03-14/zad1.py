l=[1,2,4,3,5,6,7,8,56,43,23,65,87,12,23]
print("Biggest")
BIGGEST = 0
for x in l:
    if x > BIGGEST:
        BIGGEST = x
print(BIGGEST)

l=[1,2,4,3,5,6,7,8,56,43,23,65,87,12,23]
print("Biggest at end swap")
print(l)
MAX_INDEX = 0
for i in range(len(l)):
    if l[i] > l[MAX_INDEX]:
        MAX_INDEX = i
l[MAX_INDEX], l[i] = l[i], l[MAX_INDEX]
print(l)

l=[9,8,7,100,6,22,5,4,3,2,1]
print("Sort using biggest at the end swap")
print(l)
for j in range(len(l)):
    MAX_INDEX = 0
    for i in range(len(l)-j):
        if l[i] > l[MAX_INDEX]:
            MAX_INDEX = i
    l[MAX_INDEX], l[i] = l[i], l[MAX_INDEX]
    print(l)
print(l)