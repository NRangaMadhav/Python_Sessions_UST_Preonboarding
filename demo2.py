'''emp_name
emp_dob
'''
class employees:
    emp_name=''
    emp_dob=''

obj1=employees()
obj1.emp_name="Arun"
obj1.emp_dob="1stoct"
obj2=employees()
obj2.emp_name="Kamal"
obj2.emp_dob="2ndoct"
print(obj1.emp_name)
print(obj1.emp_dob)
obj1.emp_bloodgroup="a"
print(obj1.emp_bloodgroup)
print("-----------")
print(obj2.emp_name)
print(obj2.emp_dob)
obj2.emp_bloodgroup="b"
print(obj2.emp_bloodgroup)
print('---------')
employees.emp_bloodgroup="o" #dynamically adding the class attribute

obj3=employees()
obj3.emp_name="Madhav"
obj3.emp_dob="3rdoct"
obj3.emp_bloodgroup="ab"
print(obj3.emp_name)
print(obj3.emp_dob)
print(obj3.emp_bloodgroup)
 