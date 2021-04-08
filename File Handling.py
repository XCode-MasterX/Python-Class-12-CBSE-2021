import os

user_input = input("Enter something: ") # Some input by the user.
mode = 'a' # The mode in which the file will opened in.
file_path = "C:\\Users\\HP\\Desktop\\test.txt" # The path to the file.

if os.path.exists(file_path): # Checking whether the path to the file exists or not, if it exists append to it, else create and write to it.
    mode = 'a+' # The 'a' means that the program will APPEND the input to the end of the file.
else:
    mode = 'w+' # The 'w+' means that the program will CREATE and WRITE to the file as it doesn't exist.
with open(file_path, mode) as f:
    l = f.read(50)
    if l:
        print(f.readline())
    f.write(user_input)
    print(l)
print("Done!")
