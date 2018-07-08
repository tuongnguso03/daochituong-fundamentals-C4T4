#minh_duc=["Minh Đức","Sơn La", 19, 2, 1, 10]
#dictionary/object/map
#key:value
person = {
    "name": "Đức cớp",
    "age": 19,
    "ex": 2,
    "iq": 1
}
#print(person)

#person["hometown"] = "Sơn La" #thêm con hàng mới
#print(person) 

#person["ex"] = 3 #Sửa hàng
#print(person)

#read

#for key in person.keys():
    #print(key, end ="\t")
    #In tên của các con hàng

#for key in person.keys():
    #print(person[key])
    #In nội dung của các con hàng tùy vào key

#print(person["name"])   #in con hàng có key "name"

#for values in person.values():
    #print(values)
    #In hết value của các con hàng
d=1
if d in person:
    print(1)
else:
    print(2)        