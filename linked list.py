class linkedlist():
    def __init__(self,value,nextnode=None):
        self.value=value
        self.nextnode=nextnode

node1=linkedlist('7')
node2=linkedlist('77')
node3=linkedlist('777')
node4=linkedlist('7777')

node1.nextnode=node2
node2.nextnode=node3
node3.nextnode=node4

currentnode=node1
while True:
    print (currentnode.value,"->",end=' ')
    if currentnode.nextnode is None:
        print("None")
        break
    else:
        currentnode = currentnode.nextnode
    
