class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.back=None

class Stack:
    def __init__(self):
        self.top=None


# create standalone function isPalindrome
def isPal(inputQueue):
# check to ensure that the queue as at least two nodes or it won't work 
    if inputQueue < 2:
        return False
    else:
# use a while loop to reverse the sequence of numbers into newStack
        runner = inputQueue.front
        newStack = Stack()
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