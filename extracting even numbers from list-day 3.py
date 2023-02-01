l=list(map(int,input("enter the elements: ").strip().split()))
for i in range(0,len(l)):
    if l[i]%2==0:
        print(l[i])
