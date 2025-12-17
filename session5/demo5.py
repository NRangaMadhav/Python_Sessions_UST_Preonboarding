'''read login name 
test login is root or not
try again login success
max appempts 3
break exit loop'''
i=1
while(i<=3):
    login=input("Enter the login :")
    if(login=="root"):
        print("login sucess")
        break
    else:
        print(f"try again left attempts")