#C0DE1--A list contains names of boysand girls as its elements.Boys names are stored as tuples.Write a program to find out no. of boys and girls n the list.
l=['g1','g2','g3',('b1','b2','b3','b4')]
boys_c=0;
girls_c=0;
lenn=0;
for i in l:
    if type(i)==tuple:
        lenn=len(i)
        boys_c=boys_c+lenn
    else:
        girls_c=girls_c+1
print(boys_c,girls_c)

#CODE2--A list contains tuples containing roll no,name & age of students.wrrit a program to create three lists separately for roll no, name and age
l=[(1,2,3),("het","parth","maan"),(18,19,21)]
l1=list(l[0])
l2=list(l[1])
l3=list(l[2])
print(l1,l2,l3,sep=" ")

#CODE3--A date is represtented as a tuple (d,m,y).Create two date tuples and find the no of days between the two dates.
import datetime
def tuple3():
    d1=(18,2,2025)
    d2=(18,2,2024)
    date1=datetime.date(d1[2],d1[1],d1[0])
    date2=datetime.date(d2[2],d2[1],d2[0])
    print(date1,date2)
    x=abs(date1-date2)
    print(x)
tuple3()


#CODE4--Create a list of tuples containing a food items and price.sort the items in descending order wrt to price.
import operator
l=[('burger',69),('pizza',169),('sanwich',269),('ice cream',369)]
print(sorted(l,key=operator.itemgetter(1)))


#CODE5--Remove empty tuple(s) from the lists of tuples.
l=[(1,2,3),(),('het'),(18,19),(),('parth')]
l1=[]
for i in l:
    if not i:
        continue
    else:
        l1.append(i)
print(l1)    

#CODE6--Modify an element of a tuple.
tpl=(1,2,3,4,5)
l=list(tpl)
l[2]=51
tpl=tuple(l)
print(tpl)


#code7--Delete an element of a tuple.
tpl=(1,2,3,4,5)
l=list(tpl)
l.pop(2)
tpl=tuple(l)
print(tpl)
