from os import path as p

#Function to first read and print the contents then write into the file
def readAndWriteToFile(file: str):
    try:
        readFile(file, 'r')
        writeFile(file, 'w')
    except Exception as e:
        print("There was a problem", str(e), sep = ": ")

#Function to write into the provided file after removing the previous information
def writeFile(file, closeFile = True):
    try:
        with open(file, mode) as f:
            user_input = input("Do you have multiple lines of input? (Y/N)")
            if user_input.strip().lower() in ['y', 'yes']:
                x = 'y'
                while x not in ['n', 'no']:
                    user_input = input("Enter your input: ")
                    f.write(user_input)
                    x = input("Do you have more lines of input? (Y/N)")
            elif user_input in ['n', 'no']:
                user_input = input("Enter your input: ") # Taking input from the user.
                f.write(user_input) # Writing that input into the file.
    except Exception as e:
        print("There was a problem in writing to the file", str(e), sep = ": ")

# Function to read and print the contents of the file
def readFile(file, mode):
    try:
        with open(file, mode) as f:
            for line in f:
                print(line) # Printing the content of each line of the file
    except Exception as e:
        print("There was a problem while reading in from the file", str(e), sep = ": ") # Printing the error incase one occurs

#Main program start

filepath = input("Enter the path to file: ")

if p.exists(filepath):
    modes = ['w', 'r', 'a', 'w+', 'r+', 'a+','wb', 'rb']
    mode = input("Enter the mode for the file: \n1: \'w\' \n2: \'r\' \n3: \'a\' \n4: \'w+\' \n5: \'r+\' \n6: \'a+\'")
    if mode in modes:
        if mode in ["a+", "r+", "w+"]:
            readAndWriteToFile(filepath, mode)
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
