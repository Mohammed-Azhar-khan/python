s1={"apple","mango","goa","berry"}
s2={"apple","devops","aws"}
s3=s1.intersection(s2)
print(s3)
s4=s1&s2
print(s4)
# how to changing actual set obj
s1.intersection_update(s2)
print(s1)