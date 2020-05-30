class Node:
    def __init__(self, value):
        self.value=value
        self.next=None



class Stack:
    def __init__(self):
        self.top=None
    

    def is_empty(self):
        if self.top==None:
            return False
        else:
            return True

    def push(self, value):
        newnode=Node(value)
        if self.top==None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
        return self

    def pop(self):
        if self.top!=None:
            topvalue=self.top.value
            self.top=self.top.next
            return topvalue
        else:
            return self

    def size(self):
        count = 0
        if self.top==None:
            return count
        else:
            runner = self.top
            while runner != None:
                count += 1
                runner = runner.next
            return count

def compare_stack(s, s2):
    if s.size()!=s2.size():
        return False
    else:
        runner1=s.top
        runner2=s2.top
        while runner1!=None:
            if runner1.value!=runner2.value:
                return False
            else:
                runner1=runner1.next
                runner2=runner2.next
        return True
            
s = Stack()
s2= Stack()
print(s.push("a!"))
print(s.push("b!"))
print(s.push("c!!"))
print(s.push("d!!!"))
print(s2.push("a!"))
print(s2.push("b!"))
print(s2.push("c!!"))
print(s2.push("d!!!"))
print(compare_stack(s, s2))






      






