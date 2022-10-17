import pandas as pd
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rnum = len(numbers)
cnum = len(numbers[0])
largestR=0
largestVal=0
largestRSize=-1
print ('Sum of rows: ', end=' ')
for i in range(rnum):
    rsum=sum(numbers[i])
    if rsum>largestRSize:
        largestRSize=rsum
        largestR=i
    print(rsum,end=' ')
print()
print('Sum of columns: ', end=' ')
for c in range (cnum):
    csum=0;
    for j in range(rnum):
        csum+=numbers[j][c]
        if largestVal<numbers[j][c]:
            largestVal=numbers[j][c]
    print(csum,end=" ")
print()
print(f"The row that has the greatest sum: {largestR}")
print(f"The greatest number: {largestVal}")
# ******************************
# Make your Code
# ******************************
