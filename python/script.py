#!/usr/bin/python3


#varibales
age1 = 10
age2 = 15
total = age1 + age2
print(age1 + age2)
print (total)

str1 = " sunny day "
print (str1)


fname = "giri"
lname = "uppuganti"
print(fname + " " + lname)


str2="today is sunny day"
print(str2[0:5])

##String operations

name ="jake"
sentense="%s is 15 years old"
age = "50"


## operators
print(age)

sarah = mike = 15

print (sarah)

name, age = "scott", 25
print (name)
print (age)


###Placeholders

x = 10
y = 15

print(f"sum of x and ys is {x + y}")



### List - data structures

items=['apples','bananas','oranges']
print(items[0])


print(f"{items[0]} good for health")

print(f"first 2 items {items[0:2]}")

## lists are mutable

items.append('berries')
print (items)

items[0]="cherries"
print (items)
del items[2]

print (items)


print(f"length of list {len(items)}")



list_num=[5,2,10,25,11]
print(max(list_num))
print(min(list_num))

print(list_num[1] * list_num[3])




##################################
#Dictionary


students = {'bob':12, 'john':15, 'emily':20}
print(students['bob'])
print(len(students))
print(students)


####Tuples
## Tuples are immutable; can't be modified after creation

tup1= ('oranges', 'apples', 'bananas')
tup2=(12,14)
tup3=tup1 +tup2 
print (tup1)
print (tup2)
print (tup3)

##############################
#conditional statement

if 5 > 8 :
     print ("big")
else:
     print ("small")

age=45

if age < 20 :
    print ("you are child")
elif age > 20 and age < 25:
    print ("collect student")
elif age > 20 and age < 40:
    print ("middle age")
else:
    print ("you are old")


