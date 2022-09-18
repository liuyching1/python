#有序可動列表List

li=[12,60,50,15,73]
print(li)    #[12,60,50,15,73]
print(li[3]) #15
li[2]=55
print(li)    #[12,60,55,15,73]
print(li[1:3])     #[60,55]

li[2:4]=[] #刪除
print(li) #[12,60,73]

li=li+[77,42,48] #加入
print(li) #[12,60,73,77,42,48]

length=len(li)
print(length) #6

li2=[[5,7,11,30][12,60,50,77]]
print(li2[0][2]) #11
li2[0][2:]=[5,4] 
print(li2[0])  #5,7,5,4
print(li2)  #[[5,7,5,4][12,60,50,77]]

#有序不可動列表Tuple
data=(3,4,5)
print(data) #(3,4,5)
print(data[0:2]) #(3,4)

# data[0]=5 #錯誤:Tuple資料不可動
print(data) #Error
