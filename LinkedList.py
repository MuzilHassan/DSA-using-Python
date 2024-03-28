
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None #creating empty linklist
        self.n=0       #using n to keep track of size

    def __len__(self):
        return self.n

    def __str__(self):
        cur=self.head
        result=""
        while(cur!=None):
            result=result+str(cur.data)+"->"
            cur=cur.next
        return result[:-2]

    def append(self,value):
        node=Node(value)
        if(self.head==None):
            self.head=node
            self.n+=1
            return
        cur=self.head
        while(cur.next!=None):
            cur=cur.next
        cur.next=node
        self.n+=1




    def insert_head(self,value):
        new_node = Node(value)
        if self.head==None:
            self.head=new_node
            self.n=self.n+1
            return

        new_node.next=self.head
        self.head=new_node
        self.n=self.n+1

    #Works fine
    # def after(self,aft,value):
    #     if(self.head==None): return "List is empty"
    #     new_node=Node(value)
    #     cur=self.head
    #     while(cur.data!=aft ):
    #         cur=cur.next
    #         if (cur == None): return "Value is not in list"
    #
    #     new_node.next=cur.next
    #     cur.next=new_node
    #     self.n=self.n+1

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
            return self.append(value)
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

    def search(self,value):
        if self.head==None:
            return  "List is empty"
        cur=self.head
        pos=0
        while cur!=None:

            if cur.data==value:
                return pos
            cur=cur.next
            pos += 1
        return "Not Found "
    def __getitem__(self, index):
        if self.n==0:
            return "list is empty"
        if index>self.n-1 or index<0:
            return "index out of bound"
        cur=self.head
        pos=1
        while pos<=index:
            cur=cur.next
            pos+=1
        return cur.data

a=LinkedList()

a.insert_head(8)

a.insert_head(9)
a.append(10)

a.insert_after(32,9)
a.insert(18,4)
#a.delete_front()
#a.delete_end()
a.delete_value(18)
a.traverse()
a.append(420)
a.insert(7,5)
a.insert_after(70,420)
#a.after(7,12)
print(a)
#a.delete_value(420)
print(a[5])
print(a)