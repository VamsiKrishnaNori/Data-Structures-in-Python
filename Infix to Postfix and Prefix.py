#!/usr/bin/env python
# coding: utf-8

# In[60]:


def InfixToPostfix(infix):
    from Stack import Stack
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack = Stack()
    postfix = []
    tokens = infix.split()
    
    for token in tokens:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "1234567890":
            postfix.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            toptoken = opstack.pop()
            while toptoken != '(':
                postfix.append(toptoken)
                toptoken = opstack.pop()
        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                postfix.append(opstack.pop())
            opstack.push(token)
    
    while not opstack.isEmpty():
        postfix.append(opstack.pop())
    return " ".join(postfix)


# In[62]:


print(InfixToPostfix("A * B + C"))


# In[66]:


def InfixToPrefix(infix):
    tokens = infix[::-1]
    tokens = tokens.split()
    for i in tokens:
        if i == '(':
            tokens[tokens.index(i)] = ')'
        elif i == ')':
            tokens[tokens.index(i)] = '('
    expr = " ".join(tokens)
    print(InfixToPostfix(expr)[::-1])


# In[67]:


InfixToPrefix("A + B * C")


# In[69]:


def PostfixEval(postfix):
    from Stack import Stack
    operandstack = Stack()
    tokens = postfix.split()
    
    for token in tokens:
        if token in "0123456789":
            operandstack.push(token)
        else:
            op2 = int(operandstack.pop())
            op1 = int(operandstack.pop())
            result = doMath(op1,op2,token)
            operandstack.push(result)
    return operandstack.pop()

def doMath(op1,op2,op):
    if op == '*':
        return op1 * op2
    elif op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '/':
        return op1/op2
    
def PrefixEval(prefix):
    prefix = prefix[::-1]
    return PostfixEval(prefix)


# In[16]:


print(PostfixEval('7 8 + 3 2 + /'))


# In[70]:


print(PrefixEval('+ 1 * 2 3'))


# In[ ]:




