#!/usr/bin/env python
# coding: utf-8

# In[22]:


def DecimalConverter(num,base):
    from Stack import Stack
    s = Stack()
    digits = "0123456789ABCDEF"
    
    while(num>0):
        i = num%base
        s.push(digits[i])
        num = num//base
    value = ''
    while(not(s.isEmpty())):
        value = value + s.pop()
    print(value)


# In[23]:


DecimalConverter(25,2)
DecimalConverter(25,16)


# In[24]:


DecimalConverter(10,8)
DecimalConverter(250,3)


# In[ ]:




