class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def ploshad(self):
        return self.a * self.b
    
if __name__ == "__main__":
    str_handler = Rectangle(15,30)
    print(str_handler.ploshad())