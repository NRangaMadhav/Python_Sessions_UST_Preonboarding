class employee:
    def __init__(self):
        self.empname= input("Enter name:")
        self.empid=input("Enter number:")

    def display(self):
        print(f"empname:{self.empname}  empid:{self.empid}")

obj1=employee()
obj2=employee()
obj3=employee()

for var in [obj1,obj2,obj3]:
    var.display()


