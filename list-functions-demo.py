#diff value in list
I1=["app1","true","false",16,18,5,0,"bye"]
for x in I1:
    print(x)
# case senstive object
I2=["ravi","raju","hello","hai","bye","apple","cat","dog","funtosh"]
c=I2.count("raju")
print("count raju obj::",c)
I2.reverse()
print(I2)
#accessing element using positive index
print(I2[1])
#accessing elements using negative index
print(I2[-1])
#accessing the element using slice operator
print(I2[-4:-1])
print(I2[1:])
print(I2[-4:-1])

#ascending order using sort function
I2.sort()
print("after calling sort fun:::",I2)
#descending order using sort function
I2.sort(reverse=True)
print("after calling sort fun::",I2)
 # remove 1 index obj from list
I2.pop(1)
print("after remove the 2nd index obj",I2)

I2.remove("hello")
print("after remove the hello element",I2)

 #append
I2.append("kamal")
print(" after appending element ",I2)

I3=["roja","pavan","Mass","Tata","babu"]
# adding two list obj 
I2.extend(I3)
print("after adding I3 obj::",I2)
