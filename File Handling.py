from os import path as p

#Function to first read and print the contents then write into the file
def readAndWriteToFile(file):
    try:
        readFile(file, closeFile = False)
        appendFile(file)
    except Exception as e:
        print("There was a problem", str(e), sep = ": ")

#Function to write into the provided file without removing the previous information
# The 'closeFile' variable is just in case we don't want to close file.
def appendFile(file, closeFile = True):
    try:
        user_input = input("Enter your input: ")
        file.write(user_input)
        file.close()
    except Exception as e:
        print("There was a problem in writing to the file", str(e), sep = ": ")

#Function to write into the provided file after removing the previous information
# The 'closeFile' variable is just in case we don't want to close file.
def writeFile(file, closeFile = True):
    try:
        user_input = input("Enter your input: ") # Taking input from the user.
        file.write(user_input) # Writing that input into the file.
        file.close() # Closing the file
    except Exception as e:
        print("There was a problem in writing to the file", str(e), sep = ": ")

# Function to read and print the contents of the file
# The 'closeFile' variable is just in case we don't want to close file.
def readFile(file, closeFile = True):
    try:
        for line in file:
            print(line) # Printing the content of each line of the file
        if closeFile: # If we the boolean is true, then close the file.
            file.close()
    except Exception as e:
        print("There was a problem while reading in from the file", str(e), sep = ": ") # Printing the error incase one occurs

#Main program start

filepath = input("Enter the path to file: ")

if p.exists(filepath):
    modes = ['w', 'r', 'a', 'w+', 'r+', 'a+']
    mode = input("Enter the mode for the file: \n1: \'w\' \n2: \'r\' \n3: \'a\' \n4: \'w+\' \n5: \'r+\' \n6: \'a+\'")
    if mode in modes:
        if mode == "a+" or mode == "r+" or mode == "w+":
            readAndWriteToFile(open(filepath, mode))
        elif mode == "a":
            appendFile(open(filepath, mode))
        elif mode == "r":
            readFile(open(filepath, mode))
        elif mode == "w":
            writeFile(open(filepath, mode))
    else:
        print("Sorry, the entered mode is wrong.")
else:
    print("Sorry, the file wasn't found.")

#Main program end
