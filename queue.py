class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length =+1

    def enqueue(self,value):
        new_node = Node(value)
        if self.length==0:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next = new_node 
            self.last = new_node 
        self.length=+1

    def dequeue(self):
        if self.length == 0:
            return None
        
        temp = self.first 
        self.first = self.first.next 
        self.length -= 1

        if self.length == 0:
            self.last = None

        return temp.value
    
    def print(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next

my_queque = Queue(4)
my_queque.enqueue(7)
my_queque.dequeue()
my_queque.print()
