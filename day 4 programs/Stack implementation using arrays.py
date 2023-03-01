stack=[]
def push():
    ele =int(input("enter  the element: "))
    stack.append(ele)
    print(stack)
        

def pop():
    if stack is None:
        print("stack is empty")
    else:
        stack.pop()
        print(stack)












while True:
    print("enter the operation: 1.push 2.pop 3.quit")
    choice=int(input("enter choice: "))
    if choice==1:
        push()

    elif choice==2:
        pop()

    elif choice==3:
        break
    else:
        print("you enter incorrect operation")
