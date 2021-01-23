import random

str_=input()
if str_=="GET":
    for i in range(0,6):
        print(random.randint(0,9),end="")
else:
    print("input error!")