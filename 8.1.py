#CODE 8.1
l=["hello","i","am","het"]
s=set()
for i in l:
    s.add(i.upper())
print(s)

#CODE 8.2
import random
s=set()
count=0
while len(s)<10:
    s.add(random.randint(15,45))
s1=s
print(s)
for i in s:
    if i<30:
        count+=1
for i in s.copy():
    if i>35:
        s.discard(i)
print(s1)
print(count)


#CODE 8.3
s=set()
s1={"a","b","c","d","e"}
s.update(s1)
l1=list(s)
l1[0]="z"
l1.pop(1)
l1.pop(2)
s=set(l1)
print(s)


#CODE 8.4
s={"as","bataki","agarwal","bomby","abhi"}
s1=set();s2=set()
for i in s:
    if i[0]=="a":
        s1.add(i)
    else:
        s2.add(i)
print(s1,s2)
















    
