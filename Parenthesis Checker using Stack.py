#!/usr/bin/env python
# coding: utf-8

# In[17]:


def ParChecker(Expression):
    from Stack import Stack 
    s = Stack()
    for i in Expression:
        if i in ['(','{','[']:
            s.push(i)
        elif (s.isEmpty() and i in [')','}',']']):
            return False
        elif (i == ')' and s.peek()=='('):
            s.pop()
        elif (i == ']' and s.peek()=='['):
            s.pop()
        elif (i == '}' and s.peek()=='{'):
            s.pop()
    return s.isEmpty()


# In[20]:


ParChecker('(()((())()))')


# In[21]:


ParChecker('(()((())()))(')


# In[22]:


ParChecker('(()((())())))')


# In[23]:


ParChecker('[][]]')


# In[24]:


ParChecker('[][]][]')


# In[ ]:




