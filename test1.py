num=int(input())
list1=[]
list2=[]
result=0
for i in range(0,5):
    add=num
    for j in range(0,i):
        add*=10
        add+=num
    list1.append(add)
    list2.insert(0,add)

for i in range(0,5):
    result+=list1[i]
    print(list1[i],end="+")
for i in range(1,5):
    result+=list2[i]
    if i==4:
        print(list2[i], end="=")
        break
    print(list2[i],end="+")

print(result)