#creating list

x=["app1","app2","app3","app4","app5","app6","app","10"]

# it will display 2 index obj and data type

print("2 index :::",x[2],"datatype :::",type(x))

#inserting obj

for i in x:
    print(i)

# update 2 index obj
x[2]="hai"
print("after updating 2 index:::","x[2]","datatype:::",type(x))
#update more than one obj
x[2:4]=["pavan","nani"]
print("after updating 2 objs:::","x[2]","3rd index:::",type(3))
#after third index we want insert new element
x.insert(3,"hello")
print(x)
#remove all
x.clear()
print(x)

