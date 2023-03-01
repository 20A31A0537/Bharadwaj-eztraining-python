queue=[]
def enqueue():
    ele=input("enter the element")
    queue.append(ele)
    print(queue)

def dequeue():
    if queue is None:
        print("queue is empty")
    else:
        queue.pop()
        print(queue)

def display():
    print(queue)
    
    
while True:
    ele=input("enter the operation: 1.enqueue 2.dequeue 3.display 4.quit")
    choice =int(input("enter choice: "))
    if(choice==1):
        enqueue()
    elif(choice==2):
        dequeue()
    elif(choice==3):
        display()
    elif(choice==4):
        break
    else:
        print("enter correct operation")
