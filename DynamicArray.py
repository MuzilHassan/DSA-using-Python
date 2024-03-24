import ctypes

class myList:
    def __init__(self):
        self.size=1
        self.n=0
        self.A=self.__makeArray(self.size)

    def __makeArray(self,size):
        return (size*ctypes.py_object)()

    def __len__(self):
        return self.size

    def append(self,item):
        if self.size==self.n:
           newArray=self.__makeArray(self.size*2)
           self.size=self.size*2

           for i in range(len(self.A)):
               newArray[i]=self.A[i]
           self.A=newArray
        self.A[self.n] = item
        self.n = self.n + 1

    def __str__(self):
        array=""
        for i in range(self.n):
            array=array+str(self.A[i])+","
        array="["+array[:-1]+"]"
        return array

    def __getitem__(self, index):
      if  0<=index<self.n:
          return self.A[index]
      return "IndexEroor: Index out of bound"


    def pop(self):
        if self.n==0:
            print("Array is empty")
        else:
            print(self.A[self.n-1])
            self.n=self.n-1


    def clear(self):
        self.size=1
        self.n=0

    def find(self,value):
        for i in range(self.n):
            if self.A[i]==value:
                return i
        return "Value Error : Value not in list"


    def insert(self,index,value):
        if index>self.n:
            return print("index Eroor : index out of range")
        if self.size == self.n:
            newArray = self.__makeArray(self.size * 2)
            self.size = self.size * 2

            for i in range(len(self.A)):
                newArray[i] = self.A[i]
            self.A = newArray
        a=self.n-1

        while(a>=index):
           self.A[a+1]=self.A[a]

           a=a-1
        self.n=self.n+1
        self.A[index]=value


    def __delitem__(self, key):
        if key>self.n-1 or key<0:
            return print("index Error: invalid Index")
        a=key+1
        while(a<self.n):
            self.A[a-1]=self.A[a]
            a=a+1
        print(self.A[key])
        self.n=self.n-1


    def remove(self,value):
      item=self.find(value)
      if  type(item)==int:
          self.__delitem__(item)
      else:
          print(item)

    def min(self):
        min =str(self.A[0])

        for i in range(self.n):
            if str(self.A[i])<min:
                min=str(self.A[i])
        return min

    def max(self):
        max = str(self.A[0])

        for i in range(self.n):
            if str(self.A[i]) > max:
                max = str(self.A[i])
        return max

    def extend(self,items):
        for i in items:
            self.append(i)

    def __add__(self, other):
        if type(other)!=list:
            return print("TypeError: can only concatenate list  to list")

        for i in other:
            self.append(i)

    def sum(self):
        sum=0

        for i in range(self.n):
            sum=sum+int(self.A[i])
        return sum


    def count(self,key):
        count=0
        for i in range(self.n):
            if self.A[i]==key:
                count=count+1
        return count


    def sort(self,reverse=0):
        #Using Bubble Sort Algorithm
        if reverse==1:
            for i in range(self.n):
                for j in range(self.n-1):
                    if self.A[j]<self.A[j+1]:
                        temp=self.A[j]
                        self.A[j]=self.A[j+1]
                        self.A[j+1]=temp
        else:
            for i in range(self.n):
                for j in range(self.n - 1):
                    if self.A[j] > self.A[j + 1]:
                        temp = self.A[j]
                        self.A[j] = self.A[j + 1]
                        self.A[j + 1] = temp

l=myList()
l.append(2)

l.append(8)
l.append(90)

l.insert(1000,3)
l.insert(2,2)
l.insert(3,50)
l.extend([9,0,8])
l.sort(reverse=True)
print(l)


