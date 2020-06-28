#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In this programme I took a radious from the user and found the area of the given radious
radius = int(input("  Please give the radius of your circle: "))

area = (22/7)*(radius)*(radius)
print ("The area of your circle is: " + str(area))


# In[3]:


# In this programme I asked the user to give a random file and see what extension is it.
file = input("Please a give a file name: ")
print (file)
var = len(file)
inc = 0
while inc < var :
    if file  [inc] == (".") :
           break
    inc = inc+1
print("The file extension is : " + file[inc+1:var])
    

