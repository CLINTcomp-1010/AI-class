#The list of the 10 employees 
my_list = ["clinton","terry","ose","nelson","emmanuel","segun","courtney","jerry","larry","harry"]

#list split into 2 (5 each)
SubList1= my_list[:5]
SubList2= my_list[5:]
print("first list: ", SubList1 )
print("second list: ", SubList2)

#Add new employee to SubList2
SubList2.append("kriti brown")
print(SubList2)

#remove second employee in SubList1
del(SubList1[1])
print(SubList1)

#merge both list
SubList1.extend(SubList2)

#merged_list = SubList1
print("the merged list:", SubList1)

SalaryList= [9000,4000,2000,5000,100,3000,30,6000,550,470]
for i in SalaryList:
    print(i * 0.04+ i , end=", ")