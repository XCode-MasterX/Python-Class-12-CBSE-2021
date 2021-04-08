# Stack Class
class Stack:

    #Method to initialize the object.
    def __init__(self):
        self.l = [] # Making an empty list

    # Method to add element to the end of the Stack.
    def push(self, data):
        self.l.append(data)

    # Method to remove element element from the end of the stack.
    def pop(self):
        x = self.l # Making a new list.
        val = x[len(x) - 1] # Getting the last element.
        x.remove(val) # removing the last element.
        self.l = x # Assigning the changed list back to the origianl list.

        return val # returning the value that was removed from the stack.

    def isEmpty(self):
        return len(self.l) == 0 # If the length of the list is 0, then the Stack is empty.

    def printing(self):
        if(self.isEmpty()): #Checking if the stack is empty
            return("STACK > \'EMPTY\'") # returning the 'empty' Stack as a string.
        else:
            return ("STACK > " + str(self.l)) # returning contents of the Stack as a string  only if the Stack is not empty.


# Main Program begin
stack = Stack()

while input("Enter \'Y\' to continue or \'N\' to stop: ").lower() == "y":
    val = input("Valid Commands:\n\'1\' Push\n \'2\' Pop\n \'3\' Print Stack\n Enter command: ")
    if val == "1":
        stack.add(input("Enter a value: "))
    elif val == "2":
        print("This has been removed: ", stack.remove())
    elif val == "3":
        print(stack.printing())
    else:
        print("Command is invalid")

print(stack.printing())

# Main Program End
