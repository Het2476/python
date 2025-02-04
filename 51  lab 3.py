#CODE1:Count how many vowels are there in strings.accept the string from the user
s1=input("");
s=s1.lower()
i=0
count=0;
for i in range(0,len(s)):
    if s[i]=="ä" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        count=count+1;
print(count)

#CODE3:Accept two strings.Check whether one string is there in anotheer string.
s1=input("pls give 1st string");
s2=input("pls give 2nd string");
if s1 in s2:
    print("True")
else:
    print("False")

#CODE4:Write a function that removes one string from aother string.
s1=input("pls give 1st string")
s2=input("pls give 2nd string")
snew=s1.replace(s2,"")
print(snew)

#CODE2:Write ur function to convert all characters of a string into lower/upper/toggle case
