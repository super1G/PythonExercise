#參數預設資料
def power(base,esp=0):
    print(base**esp)

power(3,2)
power(4)
#參數名稱對應
def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n2=2,n1=4)

#無限參數 *ns會被用tuple方式存取
def avg(*ns):
    # print(ns)
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))

avg(1)
avg(2,4,6,7)
avg(5,3,7,2,1)
