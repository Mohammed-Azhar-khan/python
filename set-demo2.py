s1={"apple","mango","banana","cat","dog","eagle"}
s2={"welcome","aws"}
s3={"swiggy","zomato"}
#we can aslo give this line as 5 line s4=s1 | s2 | s3
s4=s1.union(s2,s3)
print(s4)
l=["hari","hari","hari","raju","bheem","bheem"]
s5=set(l)
print ("after remove duplicates:::",s5)
t=("swiggy","swiggy","zomato","zomato","zepto","zepto")
s6=set(t)
print("after remove tuple duplicates:::",s6)

s7={"apple","mango","banana","strawberry"}
s8={"apple","aws","devop"}
s9=s7.intersection(s8)
print(s9)
s10=s7 & s8
print(s10)