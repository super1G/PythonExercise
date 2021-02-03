# List 有序可變動列表
grades=[12,50,69,99,33,42]
grades[3]=22
print(grades[3])
print(grades[1:3])
print(grades)
grades[1:3]=[]  #連續刪除
print(grades)
grades=grades+[23,63]
print(grades)
print(len(grades)) #長度顯示

data=[[1,2,3],[6,7,8]]
print(data[0][1])
data[0][0:2]=[4,4,4]
print(data)
# Tuple 有序不可變動列表
data=(3,4,5)
#data[0]=5 無法更新
print(data[0:2])
