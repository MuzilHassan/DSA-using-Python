
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0

    def __len__(self):
        return self.n

    def insert_head(self,value):
        new_node = Node(value)
        if self.head==None:
            self.head=new_node
            self.n=self.n+1
            return

        new_node.next=self.head
        self.head=new_node
        self.n=self.n+1

    def inset_end(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next=new_node
        self.n = self.n + 1

    def insert_after(self,value,after):
        new_node=Node(value)
        cur=self.head
        while(cur!=None):
            if cur.data==after:
                new_node.next=cur.next
                cur.next=new_node
                self.n=self.n+1
                return
            cur=cur.next
        print("value not found")

    def insert(self,value,pos):
        if pos>self.n:
            return print("index out of bound")
        if pos==0:
            return self.insert_head(value)
        if pos==self.n:
            return self.inset_end(value)
        index=0
        cur=self.head
        while index<pos-1:
            index=index+1
            cur = cur.next
        new_node=Node(value)
        new_node.next=cur.next
        cur.next=new_node
        self.n=self.n+1

    def traverse(self):
        cur=self.head
        while(cur!=None):
            print(cur.data)
            cur=cur.next

    def clear(self):
        self.head=None
        self.n=0

    def delete_front(self):
        if self.n==0:
            return print("List is already Empty")
        self.head=self.head.next
        self.n=self.n-1

    def delete_end(self):
        if self.n==0:
            return print("List is already Empty")
        if self.n==1:
            self.head=None
            self.n=self.n-1
            return
        cur=self.head
        while cur.next.next!=None:
            cur=cur.next
        cur.next=None
        self.n=self.n-1

    def delete_value(self,value):
        if self.n==0:
            return print("List is already Empty")

        if self.head.data==value:
            self.head=self.head.next
            self.n=self.n-1
            return

        cur= self.head
        while cur.next!=None:
            if cur.next.data==value:
                cur.next=cur.next.next
                self.n=self.n-1
                return
            cur=cur.next
        print("value not found")



a=LinkedList()
a.insert_head(8)
a.insert_head(9)
a.inset_end(10)
a.insert_after(32,9)
a.insert(18,4)
#a.delete_front()
#a.delete_end()
a.delete_value(18)
a.traverse()
