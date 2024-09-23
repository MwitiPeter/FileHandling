f= open("Data.txt","a")#a+-file pointer at end of file "r+"-at the begining
f.writelines(["\nline1","\nline2","\nline3"])
f.close()