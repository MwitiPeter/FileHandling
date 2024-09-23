import os #import statement

filename = "Example.txt"
if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} has been deleted.")
else:
    print (f"{filename} does not exist.")

