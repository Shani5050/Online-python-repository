#!/usr/bin/env python
# coding: utf-8

# # Roll No. JP15080

# ### Question 1: 

# In[6]:


print("Twinkle, twinkle, little star, \n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are"); ## Question 1 


# ### Question 2: Write a Python program to get the Python version you are using?

# In[7]:


import sys 
print(sys.version)


# ### Question 3: Write a Python program to display the current date and time.

# In[15]:


from datetime import datetime

now = datetime.now()
print(now)


# ### Question 4: Write a Python program which accepts the radius of a circle from the user and compute the area

# In[18]:


r = float(input("Please enter the radius="))
area = 3.14*r**2
print("The area of circle is=", area)


# ### Question 5: Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# In[21]:


First_name = input("First Name=")
last_name = input("Last Name=")
print(last_name+"\t"+First_name)


# ### Question 6: Write a python program which takes two inputs from user and print them addition

# In[23]:


First_input = input("Enter the first input=")
Second_input = input("Enter the Second Input=")
print (First_input+Second_input)


# ### Question 7: Write a program which takes 5 inputs from user for different subject’s marks, total it and generate mark sheet using grades ?

# In[28]:


Math = float(input("Enter the Math's marks="))
Geology = float(input("Enter the Geology marks="))
Plate_tec = float(input("Enter the plate tec marks="))
sedimentology = float(input("Enter the sedimentology marks="))
data = float(input("Enter the data's mark="))
total = Math+Geology+Plate_tec+sedimentology+data
print("The total marks are=", total)
average = total/5
print("The average is ", average)
if (average>=90):
    print("Grade A")
elif (average>=80 and average<90):
    print("Grade B")
elif (average>=70 and average<80):
    print("Grade C")
elif (average>=60 and average<70):
    print("Grade D")
else:
    print("Fail")
    
    


# ### Question 8: Write a program which take input from user and identify that the given number is even or odd?

# In[34]:


num = int(input("Enter the number="))
if (num%2 == 0) :
    print("The number is even")
else:
    print("The number is odd")


# ### Question 9: Write a program which print the length of the list?

# In[40]:


lst = ["a","b","c","d","e","f","g"]
len(lst)


# ### Question 10: Write a Python program to sum all the numeric items in a list?

# In[41]:


lst = [1,2,3,4,5]
sum(lst)


# ### Question 11: Write a Python program to get the largest number from a numeric list.
# # I am not able to solve this Question. Could you please solve it in the class. Gracious.

# ### Question 12: Take a list, say for example this one:
# ### a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# ### Write a program that prints out all the elements of the list that are less than 5.

# In[44]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for a in a:
    if a<5:
        print(a)


# In[ ]:




