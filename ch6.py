x=input("輸入數字:")
x=int(x)
if x>200:
    print("200")
elif x>100:
    print("100")
else:
    print("0")

x=int(input("輸入數字:"))
y=int(input("輸入數字:"))
op=input("輸入:+ - * / ")
if op=="+":
    print(x+y)
elif op=="-":
    print(x-y)
elif op=="*":
    print(x*y)
elif op=="/":
    print(x/y)
else:
    print("不支援") 
