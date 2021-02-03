#break
n=0
while n<5:
    if n==3:
        break
    print(n)
    n+=1
print("LAST N:",n)
# continue
n=0
for x in [1,2,3,4]:
    if x%2==0:
        continue
    print(x)
    n+=x
print("LAST X:",x)
#else

sum=0
for n in range(11):
    sum+=n
else:
    print(sum)

#整合
n=input("輸入正整數:" )
n=int(n)
for i in range(n):
    if i*i==n:
        print("整數平方根",i)
        break
else:
    print("不是整數平方根")