Emp=['101,raj,sales,pune,1000',
     '102,leo,prod,bglore,2000',
     '103,anu,sales,hyd,3000',
     '104,zion,sales,bglore,3450']
'''iterate a given list line by line
split each line into multiple values baed in , ->do multiple initialization
display -emp name in title case format
emp workin city in upper
calcualate sum if emp's cost-display total cost at the end of the line
-----
filter -sales depts
display-emp name in title case format
emp working city in upper
calc sum if sales dept emp's cost-display sales dept total cost ar the end of the line
-------
write a function-pass dept name as argument
filter -sales dept
display-emp name in title
emp working cuty in upper case format

'''

#1
# total=0
# for var in Emp:
#     # print(var)
#     # print(var.split(','))
#     eid,ename,edept,ecity,ecost=var.split(',')
#     print(eid,ename,edept,ecity,ecost)
#     total=total+int(ecost)
#     print(f'Emp name: {ename}\t City:{ecity.upper()}')
# else:
#     print(f'\t Sum of emp cost:{total}')


#2
# for var in Emp:    
#     if edept=='sales':
#         eid,ename,edept,ecity,ecost=var.split(',')
#         print(f'Emp name: {ename.title()}\t City:{ecity.upper()}')
#         total=total+int(ecost)    
#     else:
#         print(f'\t Sum of emp cost:{total}')

#3    
def department(empdept):
    total=0
    for var in Emp:    
        if empdept in var:
            eid,ename,edept,ecity,ecost=var.split(',')
            print(f'Emp name: {ename.title()}\t City:{ecity.upper()}')
            total=total+int(ecost)  
        else:
            s='input dept  {empdept0} not found}'
            if(s):
                return s  
    else:
        print(f'\t Sum of emp cost:{total}')

department('dept')
department('sales')
department('prod')