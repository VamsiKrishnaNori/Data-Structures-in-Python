#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Stack:
    
    def __init__(self):
        """
        This function initializes the stack
        """
        self.items = []
    
    def isEmpty(self):
        """
        This function checks if the stack is empty
        :return: Boolean
        """
        return self.items == []
    
    def push(self, item):
        """
        This function pushes an item into the stack
        :param item: value
        """
        self.items.append(item)
        
    def pop(self):
        """
        This function pops the last element out of the stack
        """
        return self.items.pop()
    
    def peek(self):
        """
        This function peeks into the stack and returns the top values
        :return: value
        """
        return self.items[len(self.items)-1]
    
    def size(self):
        """
        This function retruns the size of the stack
        :return: value
        """
        return len(self.items)
    
    def getValueAt(self, index):
        """
        This function gets the value at an index pecified in the stack if exists
        :param index: integer
        :return: value
        """
        return self.items[index]
    
    def PrintValues(self):
        """
        This function prints all the elements in the stack from top
        """
        for i in range(len(self.items)-1,-1,-1):
            print(self.items[i])

