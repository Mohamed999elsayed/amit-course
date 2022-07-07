#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# ## Test your knowledge. 
# 
# ** Answer the following questions **

# ## Strings

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

# In[1]:


s = 'hello'
# Print out 'e' using indexing
print(s[1])


# Reverse the string 'hello' using slicing:

# In[2]:


s ='hello'
# Reverse the string using slicing
print (s[::-1])


# Given the string hello, give two methods of producing the letter 'o' using indexing.

# In[4]:


s ='hello'
# Print out the 'o'

# Method 1:

print(s[-1])


# In[5]:


# Method 2:
print(s[4])


# ## Lists

# Build this list [0,0,0] two separate ways.

# In[9]:


# Method 1:
my_list=[0,0,0]
print(my_list)


# In[10]:


# Method 2:
my_list=0,0,0
print(list(my_list))


# Reassign 'hello' in this nested list to say 'goodbye' instead:

# In[11]:


list3 = [1,2,[3,4,'hello']]

list3[2][2]


# Sort the list below:

# In[12]:


list4 = [5,3,4,6,1]
print(sorted(list4))


# ## Dictionaries

# Using keys and indexing, grab the 'hello' from the following dictionaries:

# In[13]:


d = {'simple_key':'hello'}
# Grab 'hello'
print(d["simple_key"])


# In[14]:


d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d["k1"]["k2"])


# In[15]:


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
print(d["k1"][0]['nest_key'][1])


# In[16]:


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#Grab hello
d["k1"][2]["k2"][1]['tough'][2]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[22]:



x = "Earth"
diameter = 12742
print(f"The diameter of {x} is {diameter}")


# ** Given this nested list, use indexing to grab the word "hello" **

# In[1]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[23]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst[3][1][2]


# ** Given this nested dictionary grab the word "hello". **

# In[21]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[ ]:


d["k1"][3]["tricky"][3]["target"][3]


# ### Write a Python program to swap two variables.
# 

# In[ ]:





# ## Thanks
