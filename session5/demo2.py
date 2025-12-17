'''python program
read a shell name from stdin
test1-test input shell name bash-initialise profile filename /etc/bashrc
test2 ksh-/etc/fskrc
test3 csh or tcsh -/etc/profile
test4 psh-c:\\win\\profile
default /bin/nologin
default profilename:/etc/profile

display shell name and profile filename'''

print("bash,ksh,vsh/tcsh,pash")
shell= input("Enter the shell name:")
if(shell=="bash"):
    profilename="/etc/bashrc"
elif(shell=="ksh"):
    profilename="/etc/fskrc"
elif(shell=="csh" or "tcsh"):
    profilename="/etc/profile"
elif(shell=="psh"):
    profilename="c:\\win\\profile"
else:
    shell="/bin/nologin"
    profilename="/etc/profile"  
print(f"shell name:{shell} profile filename:{profilename}")
