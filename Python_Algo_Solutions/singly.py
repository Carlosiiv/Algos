class SLL:
    def __init__(self):
        self.head = None


    def contains(self, n):                  
        if self.head==None:
            return False
        else:
            runner=self.head
            while runner.next != None:
                if runner.value==n:
                    return True
                runner=runner.next
                if runner.value==n:
                    return True
                else:
                    return False

    def addtofront(self, n):
        if self.head==None:
            self.head=Node(n)
        else:
            a = Node(n)
            a.next=self.head
            self.head=a
        



class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None



class SLL:
    def __init__(self):
        self.head = None

    def addtoback(self, value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode 
        else:
            #runner is created to have a variable i can use to iterate to singly linked list
            runner = self.head
            #use a while loop to iterate
            print(runner.next) #this would print a node object
            while runner.next != None:
                runner = runner.next
            runner.next = newnode
        return self

class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None



class SLL:
    def __init__(self):
        self.head = None

    def append(self, value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode 
        else:
            #runner is created to have a variable i can use to iterate to singly linked list
            runner = self.head
            #use a while loop to iterate
            # print(runner.next) #this would print a node object
            while runner.next != None:
                runner = runner.next
            runner.next = newnode
        return self

    def display(self):
        print (self.head)
        runner = self.head
        outputstr = ""
        while runner !=None:
            outputstr += f"{runner.value}-->"
            runner = runner.next

        print(outputstr)
        return self

    def addtoFront(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode
        return self

    def contains(self, valueToFind):
        if self.head == None:
            return False
        else:
            runner = self.head
            while runner != None:
                if runner.value == valueToFind:
                    print("true")
                    return True
                else:
                    runner = runner.next
            print("false")
            return False






    def remove_front(self):
        if self.head == None:
            return False
        else:
            self.head=self.head.next

    def remove_back(self):
        if self.head==None:
            return False
        else:
            runner = self.head
            while runner.next.next != None:
                runner=runner.next
            runner.next = None
        return self

class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def min_to_front(self):
        if self.head==None:
            return False
        minimum = self.head.value
        runner =self.head
        #iterate
        while runner.next != None:
            if minimum.value > runner.next.value:
                prev = runner
                minimum = runner.next.value
                minnode=runner.next
            runner=runner.next
        prev.next = prev.next.next
        minnode.next=self.head
        self.head = minnode
        return True
    
    def maxtoback(self):
        if self.head==None:
            return False
        maximum = self.head
        prev = self.head
        runner = self.head
        while runner.next!= None:
            if maximum.value < runner.next.value:
                prev = runner
                maximum=runner.next
            runner = runner.next
            prev.next = runner.next
        runner.next = maximum
        maximum.next = None
        return True    
        

     def appendVal(self, inputValue, after=None):
        if after == None or self.head == None:
            self.addToBack(inputValue)
        else:
            newNode = Node(inputValue)
            runner = self.head
            while runner.next != None:
                if runner.value == after:
                    newNode.next = runner.next
                    runner.next = newNode
                    return self
                runner = runner.next
            self.addToBack(inputValue)
            return self