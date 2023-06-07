#!/usr/bin/env python
# coding: utf-8

# In[13]:


y = input("What's the equation you want to solve (input with x): ")
t = float(input("What's the tolerance?: "))
a = 0
b = 0.2


# In[14]:


def f(x):
    G=eval(y)
    return G

print(f(a))
print(f(b))


# In[15]:


while f(a) >= 0 and f(b) <= 0:
    if f(a) < f(a + 0.2):
        a = a - 0.2
    if f(a) > f(a + 0.2):
        a = a + 0.2
    if f(b) < f(b + 0.2):
        b = b + 0.2
    if f(b) > f(b + 0.2):
        b = b - 0.2
    


# In[16]:


print(a)
print(b)


# In[ ]:




