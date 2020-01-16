# Stack module
An example of a stack in Python 3

## Example usage
```python
import stackmodule
from stackmodule import stackTools
from random import randint as rand

stackOptions = {
    'pointer': -1,
    'size': 5,
    'type': int
}

stackHandler = stackTools()


stackHandler.stackOptions = stackOptions
stackHandler.stack = stackHandler.initStack(stackOptions['size'],stackOptions['type'])

print(stackHandler.dump())

stackHandler.push(3)
print(stackHandler.dump())
for i in range (0,rand(0,30)):
    try:
        n=rand(0,651)
        stackHandler.push(n)
        print(f'Added {n}')
    except stackmodule.StackFull: print("Stack got full")

print(stackHandler.dump())
print(stackHandler.pop())
print(stackHandler.dump())
stackHandler.push(5)
print(stackHandler.dump())


stack = stackHandler.dump()

print("The script exported the stack: "+str(stack))
```

## Module features

### Making a stack handler
```python
stackHandler=stackTools(myStack,stackOptions)#Define our stack handler
```
A stack handler will simply hold the stackTools class with your stack and it's options

#### Initialise stack (initStack)
```python
stack=stackHandler.initStack(5,int) # Initialise a new stack which can contain 5 integer values
```
Initialise stack will update the list that is acting as a stack to the correct size with the expected data format

## This will most likely never be updated