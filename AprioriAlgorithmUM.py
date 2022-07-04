import numpy as np
from datetime import datetime
#load UM data
print("\nloading data... \n", datetime.now())
umpdata = np.loadtxt("UniversalMarketPlaceData.txt", dtype=int)
print(umpdata)
#function for C1 for-loop
def isInData(a, b, umpdata):
    ct = 0
    for x in range(0, len(umpdata)):
        if (a == umpdata[x,0] or a == umpdata[x,1]):
            if (b == umpdata[x,0] or b == umpdata[x,1]):
                ct = ct + 1
    return ct
#support and confidence values
support = 2
confidence = .25 #25% confidence
#Creating C1
print("\ncreating C1 list... \n", datetime.now())

C1 = np.empty((0, 2))
for x in range(0, 290):
    ct = int(np.count_nonzero(umpdata == x))
    if ct >= support:
        C1 = np.vstack((C1, [x, ct]))
#Creating C2
print("\ncreate C2 list", datetime.now())
C2 = np.empty((0, 3))
ItemC1 = C1[:,0]
for y in range(0, len(ItemC1)):
    for z in range(y+1, len(ItemC1)):
        ct = isInData(ItemC1[y], ItemC1[z], umpdata)
        print(ItemC1[y], ItemC1[z], ct)
        if ct >= support:
            C2 = np.vstack((C2, [ItemC1[y], ItemC1[z], ct]))
#Associative rules
print("\nassociative rules", datetime.now())
for g in range(0, len(C2)):
    con1 = int(C2[g][2])/int(np.count_nonzero(umpdata == C2[g][0]))
    if con1 >= confidence:
        #Will print only associative rules >= 0.25
        print(C2[g][0], '->', C2[g][1], 'The confidence level is:', con1)
    con2 = int(C2[g][2])/int(np.count_nonzero(umpdata == C2[g][1]))
    msg = 'Do not make rule'
    if con2 >= confidence:
        #Will print only associative rules >= 0.25
        print(C2[g][1], '->', C2[g][0], 'The confidence level is:', con2)

print('\nprogram finished', datetime.now())

