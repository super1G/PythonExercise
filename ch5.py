# 集合運算
s={3,4,5}

print(1  in s)
print(1 not in s)
s1 ={3,4,5}
s2 ={4,5,6,7}
s3=s1&s2 #AND
print(s3)
s3=s1|s2 #OR
print(s3)
s3=s1-s2 #差及
print(s3)
s3=s1^s2 #反交集 NAND
print(s3)

s=set("HELLO") #set(字串) 自動猜解成集合
print(s)
print("H" in s)
print("h" in s)
#字典運算

dic={"apple":"蘋果","bug":"蟲"}
print(dic)
print(dic["apple"])
dic["apple"]="小蘋果"
print(dic["apple"])
print("apple" in dic)
print(dic)
del dic["apple"]
print(dic)

dicc={x:x*2 for x in [3,4,5]}
print(dicc)