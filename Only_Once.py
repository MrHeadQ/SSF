Int_Num=[2,8,6,2,7,3,9,2,8,6,7,9,1]
Int_Num.sort()
if Int_Num[0]!=Int_Num[1]:
    print(Int_Num[0])
for i in range(1,len(Int_Num)-2):
    if Int_Num[i-1]!=Int_Num[i] and Int_Num[i]!=Int_Num[i+1]:
        print(Int_Num[i])

if Int_Num[len(Int_Num)-1] != Int_Num[len(Int_Num)-2]:
    print(Int_Num[len(Int_Num)-1])