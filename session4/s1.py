#write a program
#initialise a product name,product id,product cost
#cal sum of profucsts including tax
#display profuct details -use print()
#Expected OP:
#Product name is :pa
# product cost is:1000
# 18% tax is:180
# total including tax:1180 rs

product_name=input("Enter product name:")
product_id=int(input("id: "))
product_cost=float(input("enter cost :"))
tax=18/100*product_cost
summ=tax+product_cost
#DEMO1
# print("Product name is:"+product_name)
# print("Product cost:",product_cost)
# print("16% tax is : ",tax)
# print("total cost including tax:",str(summ))
#DEMO2
# print(f"Product name is:{product_name}")
# print(f"Product cost:{product_cost}")
# print(f"16% tax is : {tax}")
# print(f"total cost including tax:{summ}")
#DEMO3
print(f'''Product name is:{product_name}
Product cost:{product_cost}
16% tax is : {tax}
total cost including tax:{summ}''')

