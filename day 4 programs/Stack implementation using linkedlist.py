class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.head=None

    def isempty(self):
        if self.head==None:
            return True
        else:
            return False

    def push(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            nn=node(data)
            nn.next=self.head
            self.head=nn

    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head=self.head.next
            poppednode.next=None
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        t=self.head
        if self.isempty():
            print("stack underflow")
        else:
            while (t!=None):
                print(t.data,end=" ")
                t=t.next
                if(t!=None):
                    print("->",end=" ")
            return


if __name__ == "__main__":
    s=stack()
    s.push(100)
    s.push(200)
    s.push(300)
    s.push(400)
    s.display()
    print("\n")
    print(s.peek())  #printing top element of stack
    s.pop()
    s.display()
    print("\n")
    s.pop()
    s.display()
