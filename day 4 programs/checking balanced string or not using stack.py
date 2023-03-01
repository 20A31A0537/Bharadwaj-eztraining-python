s=input()
st=[]
balance=True
for char in s:
    if(char=="(" or char=="[" or char=="{"):
        st.append(char)
    elif(char==")"):
        if(len(st) and st.pop() != "("):
            balance=False
            break
    elif(char=="]"):
        if(len(st) and st.pop() != "["):
            balance=False
            break
    elif(char=="}"):
        if(len(st) and st.pop() != "{"):
            balance=False
            break
    else:
        balance=False
        break

if(balance==0 or len(st)):
    print("not balanced")
else:
    print("balanced")
