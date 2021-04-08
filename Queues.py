# Queue Class
class Queue:

    # Method to initialise the object
    def __init__(self):
        self.l = [] # Making an empty list

    #Method to add element to the beginning of the Queue
    def add(self, data):
        self.l = [data] + self.l

    def remove(self):
        x = self.l # Making a new list.
        val = self.l[0] # Getting the first element.
        x.remove(self.l[0]) # Removing the first element of the Queue
        self.l = x # Assigning the changed list back to the origianl list.

        return val # Returning the value that was removed from the Queue.

    def isEmpty(self):
        return len(self.l) == 0 # If the length of the list is 0, then the Stack is empty.

    def printing(self):
        if(self.isEmpty()): #Checking if the stack is empty
            return("QUEUE > \'EMPTY\'") # returning the 'empty' Queue as a string.
        else:
            return ("QUEUE > " + str(self.l)) # returning contents of the Queue as a string  only if the queue is not empty.

# Main program Begin
queue = Queue()
    
while input("Enter \'Y\' to continue or \'N\' to stop: ").lower() == "y":
    val = input("Valid Commands:\n\'1\' Push\n \'2\' Pop\n \'3\' Print Stack\n Enter command: ")
    if val == "1":
        queue.add(input("Enter a value: "))
    elif val == "2":
        print("This has been removed: ", queue.remove())
    elif val == "3":
        print(queue.printing())
    else:
        print("Command is invalid")

print(queue.printing())

# Main Program End
