class employee:
    def __init__(self):
        self.empname= input("Enter name:")
        self.empid=int(input("Enter number:"))
    def __str__(self):
        return str(self.empname,self.empid)
    def __call__(self):
        print(f"empname:{self.empname}  empid:{self.empid}")
        # print(f"empname:{self.empname}  empid:{self.empid}")
        return self.empname,self.empid

    # def display(self):
    #     print(f"empname:{self.empname}  empid:{self.empid}")

obj1=employee()
obj2=employee()
obj3=employee()
print(str(obj1()))
print(str(obj2()))
print(str(obj3()))
# for var in [obj1]:
#     var.display()