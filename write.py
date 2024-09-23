# open file for writing
file = open("example.txt","w") #mode method #x-create file #r- read w-write a-append 
             #filepath #access mode
#write some text to the file
file.write("Hello , world!\n")
file.write("This is a test.\n")

#close the file
file.close()