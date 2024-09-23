# with open ("<path>", "<mode>") as <var>:

class MyContextManager:
    def __enter__(self):
        print("entering context")
        return self
    def __exit__ (self, exc_type,exc_val,exc_tb):
        print ("Exiting context")
        if exc_type is not None:
            print (f"an error of type{exc_type} occured: {exc_val}")
            return True
with MyContextManager() as cm:
    print("inside context")        