#!/usr/bin/env python
# coding: utf-8

# Q1. Create one variable containing following type of data:
# (i) string
# (ii) list
# (iii) float
# (iv) tuple
# 
# 
# 

# In[1]:


a="adarsh"
b=[1,2,3]
c=21.5
d=("dsa","development")
li_1=[a,b,c,d]


# In[2]:


print(li_1)


# 
# 
# Q2. Given are some following variables containing data:
# (i) var1 = ‘ ‘
# (ii) var2 = ‘[ DS , ML , Python]’
# (iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
# (iv) var4 = 1.
# What will be the data type of the above given variable.
# 
# 

# In[5]:


var1 = ''
var2 = '[ DS , ML , Python]'   
var3 = ['DS' , 'ML' , 'Python']
var4 = 1


# In[7]:


print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))


# 
# 
# Q3. Explain the use of the following operators using an example:
# (i) /
# (ii) %
# (iii) //
# (iv) **
# 
# 

# 1-> / it is a division opertor used for divide of two operands
# 2-> % modulus operator , use for finding remainder 
# 3-> // floor division operator, used for finding non decimal part of division
# 4-> ** power operator , used for finding power of any operand

# In[9]:


a=5/2
b=6%4
c=10//3
d=2**4
print(a)
print(b)
print(c)
print(d)


# 
# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
# element and its data type.
# 
# 

# In[12]:


lis_1=["my","name","is","adarsh",19,"years","age",(1,2,3),90.5,False]
for i in lis_1:
    print(i)


# 
# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.
# 

# In[20]:


A=200
B=20
count = 0
while A % B == 0:
	A = A // B
	count += 1
print(count)


# 
# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.
# 

# In[25]:


import random

l1 = []
for i in range(0, 25):
    a = random.randint(0, 9)
    l1.append(a)
print(l1)

#second part

for i in l1:
    if i % 3 == 0:
        print(f"The element {i} is divisible by 3.")
    else:
        print(f"The element {i} is not divisible by 3.")


# 
# 
# Q7. What do you understand about mutable and immutable data types? Give examples for both showing
# this property.
# 

# mutable data types- those data type which can be changed or modified 
# example- list 
# 
# immutable data type- those data types which can not be changed , modified or re assigned.
# example-string

# In[27]:


print(l1[5])
#modified
l1[5]=10
print(l1[5])


# In[30]:


a="adarsh"
print(a[5])
#lets try to modify 
a[5]='k'
print(a[5])


# In[ ]:




