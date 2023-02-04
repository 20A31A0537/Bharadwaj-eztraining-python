boy=input("Enter boy name: ").lower()
girl=input("Enter girl name:").lower()
boy=boy.replace(" ","")
girl=girl.replace(" ","")
print(boy)
print(girl)

for i in boy:
    for j in girl:
        if i==j:
            boy=boy.replace(i," ",1)
            girl=girl.replace(j," ",1)
            break
count=len(boy+girl)
print(count)
if count>0:
    list1=["FRIENDS","LOVERS","AFFECTIONATE","MARRIAGE","ENEMIES","SIBLINGS"]
    while len(list1)>1:
              c=count%len(list1)
              s_index=c-1
              
              if s_index>=0:
                 left=list1[:s_index]
                 right=list1[s_index+1:]
                 list1=right+left
              else:
                  list1=list1[:len(list1)-1]
    print("Relationship: ",list1[0])
else:
    print("Enter different names" )
              
