# Node class
class Node:
    def __init__(self, data): # Method to initialise the node object.
        self.data = data # The data to be stored in the node.
        self.next = None # Variable to store the object of the next node.

    def add(self, data):
        if self.next != None: # Checking if the 'next' object has some value in it.
            self.next.add(data) # If the 'next' node has already been initialised then pass the data to it.
        else:
            self.next = Node(data) # If the 'next' node has no value assigned to it, then add an object to it.

    def nodePrint(self):
        if self.next:
            type_of_data = str(type(self.data))
            type_of_data = type_of_data.replace("<", "")
            type_of_data = type_of_data.replace(">", "")
            type_of_data = type_of_data.replace("class", "")
            print(self.data, type_of_data, sep = " :: ", end = " -> ")
            self.next.nodePrint()
        else:
            type_of_data = str(type(self.data))
            type_of_data = type_of_data.replace("<", "")
            type_of_data = type_of_data.replace(">", "")
            type_of_data = type_of_data.replace("class", "")
            print(self.data, type_of_data, sep = " :: ")

# LinkedList class
class LinkedList:
    
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head != None:
            self.head.add(data)
        else:
            self.head = Node(data)
            
    def listPrint(self):
        self.head.nodePrint()


#Main Program Start

linked = LinkedList()

linked.add(5)
linked.add("name")
linked.add(True)

linked.listPrint()
#Main Program End