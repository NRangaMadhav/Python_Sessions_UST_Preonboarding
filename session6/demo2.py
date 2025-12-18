'''write a program
create empty dict
        display no of items in dict
        use while loop limit 5
                read a product id from ip
                read profuct cost from ip
                add ip details in dict
                    dict key->productid
                    dict value->product cost
use for loop to display key value
display no of items from disct=>5'''
products={}
print(len(products))
items=0
while items <5:
    product_id=input("Enter prodcut id:")
    product_cost=input("Enter product cost:")
    products[product_id]=product_cost
    items+=1
print("details of the products:")
for var in products:
    print(f"{var}:{products[var]}")
print(len(products))
