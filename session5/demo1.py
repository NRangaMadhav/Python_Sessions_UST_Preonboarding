'''write a python code:
read a port number from stdin
test input port range 5001 -5999
initialise app name is demoApp
if port range is not matches with above range 
initialize app name as testApp
display app name running port number'''

port=int(input("Enter the port number:"))
if port in range(5001,6000):
    app='demoApp'
else:
    app='testApp'
print(f"App name: {app} running: {port}")