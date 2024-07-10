eid=int(input("Enter Eid"))
ename=input("Enter Ename")
esal=int(input("Entr a sal"))
deptno=int(input("Enter a deptno"))
comm=int(input("Enter a comm"))
if esal>15000 and deptno==1 and comm!=0:
    esal=esal+5000
    print(eid,":::",ename," ",esal," ",deptno," ",comm)
else:
    print("the person is the  not eligable for incre")