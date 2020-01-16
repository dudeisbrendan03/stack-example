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