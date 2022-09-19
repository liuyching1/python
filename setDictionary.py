#集合Set
s={3,4,5}
print(5 in s)  #True
print(10 not in s)  #True

s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2  #交集: 取兩個集合中相同資料
print(s3) #{4,5}

s4=s1|s2  #聯集: 取兩個集合中所有資料,但不重複取
print(s4) #{3,4,5,6,7}

s5=s1-s2  #差集: 從'前項'減去'後項'重疊資料
print(s5) # {3}

s6=s1^s2  #反交集: 取兩個集合中不重複資料
print(s6) #{3,6,7}

s=set("HiPython") #將字串拆結成集合
print("I" in s) #False

#字典Dictionary Key-value配對
dic={"phone":"手機","ice":"冰淇淋"}
print(dic["phone"]) #手機
dic["phone"]="iPhone手機" #經過指令修改字典的內容
print(dic["phone"]) #iPhone手機

dic={"phone":"iPhone手機","ice":"冰淇淋"}
print("phone" in dic) #True     檢查Key是否存在字典裡
print("banana" in dic) #False
print("banana" not in dic) #True

dic={"phone":"iPhone手機","ice":"冰淇淋"} 
print(dic) # {'phone':'iPhone手機','ice':'冰淇淋'} 
del dic["phone"] #刪除字典的鍵值對
print(dic) # {'ice':'冰淇淋'}

dic={i:i*2 for i in [3,4,5]} #dic={i:i*2 for i in 列表} 從列表內容產生字典
#if i is 2, i*2 is 4
print(dic) #{3: 6, 4: 8, 5: 10}
