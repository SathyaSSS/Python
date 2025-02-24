class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = node()

    def append(self,data):
        newnode = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newnode

    def length(self):
        total = 0
        cur = self.head
        while cur.next != None:
            total+=1
            cur = cur.next
        return total

    def display(self):
        l=[]
        cur = self.head
        while cur.next != None:
            cur = cur.next
            l.append(cur.data)
        print(l)

    def get(self,index):
        if index >= self.length():
            print("Error")
            return None
        curindex = 0
        cur = self.head
        while True:
            cur = cur.next
            if curindex == index :
                return cur.data
            curindex+=1

    def delete(self,index):
        if index >= self.length():
            print("Error")
            return None
        curindex = 0
        cur = self.head
        while True:
            lastnode = cur
            cur = cur.next
            if curindex == index:
                lastnode.next = cur.next
                return None
            curindex+=1
            
        
        
obj=linkedlist()

obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.append(5)

obj.display()
print(obj.get(2))

obj.delete(1)
obj.display()
obj.delete(1)
obj.display()













            

    
