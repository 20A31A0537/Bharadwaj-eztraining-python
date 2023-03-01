class node:
    def __init__(self,data):
        self.data= data
        self.next=None

class queue:
    def __init__(self):
        self.head=None
        self.last=None

    def enqueue(self,data):
        if self.last is None:
            self.head=node(data)
            self.last=self.head
        else:
            self.last.next=node(data)
            self.last=self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return


a_queue= queue()
while True:
    print("enqueue <value>")  #split string and integer
    print("dequeue")
    print("quit")
    
    do=input("what would you like to do").split()
    operation=do[0].strip().lower()
    if(operation == "enqueue"):
        a_queue .enqueue(int(do[1]))  #split string and integer
    elif operation =="dequeue":
        dequeued=a_queue.dequeue()
        if dequeued is None:
            print("queue is empty")
        else:
            print("queue element",int(dequeued))

    elif operation == "quit" :
        break
            
        
    
    
            
            
        
