from Prediction import *

n=col
m=row
w='n'
FirePlace1 = FirePlace(n,m,w,34)
for i in range(151,155):
    for j in range(123,129):
        FirePlace1.Inital_Fire(i,j)
Res(FirePlace1)