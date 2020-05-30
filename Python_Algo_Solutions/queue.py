class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.back=None

    def enqueue(self, value):
        newnode=Node(value)
        if self.front==None:
            self.front=newnode
            self.back=newnode
        else:
            self.back.next=newnode
            self.back=self.back.next
        return self

    
    def dequeue(self):
        if self.front == None:
            return None
        else:
            valtoreturn = self.front.val
            # frontToDequeue = self.front
            self.front = self.front.next
            # frontToDequeue.next = None
            return valtoreturn
            
    def front(self, value):
        if self.front!=None:
            return self.front.value
        else:
            return None

    def contains(self, value):                  
        if self.front==None:
            return False
        else:
            runner=self.front
            while runner.next != None:
                if runner.value==value:
                    return True
                runner=runner.next
                if runner.value==value:
                    return True
                else:
                    return False      
        
    def size(self):
        count=0
        if self.front==None:
            return 0
        else:
            runner=self.front
        while runner!=None:
            count+=1
            runner=runner.next
        return count
            
                                      

    def is_empty(self):
        if self.front==None:
            return True
        else: 
            return False
        
    

# newQueue=Queue()
# newQueue.enqueue(5)
# newQueue.enqueue(8)
# newQueue.enqueue(15)
# print(newQueue.dequeue())










def queueisPal(q):
    print(someQueue)
    runner = someQueue.front
    testString = ""
    while runner != None:
        testString += f"-{runner.value}-"
        runner = runner.next

    print(testString)
    result = isStringPalindrome(testString)

    return result

def isStringPalindrome(stringinput):
    for i in range(len(stringinput)//2):
        if stringinput[i] != stringinput[len(stringinput)-1-i]:
            return False
    return True




queue1 = Queue()
queue1.enqueue(5).enqueue(8).enqueue(18).enqueue(5)

print(queueisPal(queue1))


# create standalone function isPalindrome
def isPal(inputQueue)
# check to ensure that the queue as at least two nodes 
    if inputQueue < 2:
        return False
    else:
# use a while loop to reverse the sequence of numbers into newStack
        runner = inputQueue.front
        newStack = Stack
        while runner != None:
            newStack.push(runner.value)
            runner = runner.next
# use a second while loop to compare inputQueue and newStack
        runner = inputQueue.front
        stackRunner = newStack.top
        while stackRunner != None:
            if newStack.pop != runner.value:
                reutrn False
            else:
                runner = runner.next








