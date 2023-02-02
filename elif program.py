temp=int(input("enter the temperature: "))
if temp>45:
    print("Its hot")
elif temp>35 and temp<40:
    print("its warm")
elif temp>20 and temp<35:
    print("Its moderate")
elif temp>10 and temp<20:
    print("Its cold")
else:
    print("Its very cold")
