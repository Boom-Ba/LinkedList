# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.rear =self.front =None 
    #Function to push an element into the queue.
    
    def push(self, item): 
        #enque at rear 
        newNode =Node(item)
        if self.isEmpty():
            self.rear =self.front=newNode
            return 
        self.rear.next=newNode
        self.rear=newNode
        
         #Add code here
    def isEmpty(self):
        return self.front==None
        
    #Function to pop front element from the queue.
    def pop(self):
        #pop front
        if self.isEmpty():
            return -1
        node=self.front
        self.front =node.next
        if self.front==None:
            self.rear =None
        return node.data if node else -1 
         

