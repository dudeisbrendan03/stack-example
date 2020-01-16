"""

Stack functionality



Options:
size: the size the stack is initialised at
pointer: pointer for the stack (where data will be added/removed)
type: what type of data should the stack store
"""
#Exceptions
class StackFull(Exception):
    """Attempted to push to the stack while there is no free space"""

class StackEmpty(Exception):
    """Attempted to pop from stack while the stack while the pointers are matching (stack is empty)"""

class StackExists(Exception):
    """Tried to initialise the stack while it already exists"""

class StackMissing(Exception):
    """The stack or it's options are missing and therefore an action failed to perform"""

class StackError(Exception):
    """Failed to complete operation on the stack for an unknown reason"""


#Stack functions
class stackTools(object):
    """Stack management class"""

    def __init__(self):
        self.stackOptions = {}
        self.stack = []

    def initStack(self,size,stackType):
        if len(self.stack) != 1:
            for i in range(0,size):
                if stackType == str:   self.stack.append('')#Only time push is used - to init the stack
                elif stackType == int: self.stack.append(0)
                else: raise ValueError
            print(f'Stack it being initialised to {self.stackOptions["size"]}')
            return self.stack
        else: raise StackExists

    def push(self,content):
        if isinstance(content,self.stackOptions['type']):
            try:
                if self.stackOptions['pointer'] == self.stackOptions['size']-1: raise StackFull
                self.stack[self.stackOptions['pointer']+1] = content
                self.stackOptions['pointer']+=1
            except IndexError: raise StackFull
        else: raise ValueError

    def pop(self):
        store = self.stack[self.stackOptions['pointer']]
        if self.stackOptions['pointer'] == -1: raise StackEmpty
        else:
            self.stackOptions['pointer']-=1
            return store

    def checkFull(self):
        return self.stackOptions['pointer'] == (self.stackOptions['size'-1])

    def checkEmpty(self):
        return self.stackOptions['pointer'] == -1

    def dump(self):
        return str(self.stack)