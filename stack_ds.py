# Write a program to perfrom push,pop and display operation on stack.
n=int(input("Enter No of Operation"))
stack=[]
for i in range(n):
    cmd=input("Choose the command (push,pop,display)")
    if cmd=="push":
        value=int(input("Enter The Value"))
        stack.append(value)
        print(f'{value} Pushed Inside Stack')
    elif cmd=="pop":
        if len(stack)==0:
            print("Stack Is Empty")
        else:
            value=stack.pop()
            print(f'{value} Poped from stack')
    elif cmd=="display":
        print("The Stack Is :",stack)