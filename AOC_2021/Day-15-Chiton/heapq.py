#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
import heapq


# In[2]:


# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)


# In[3]:


# printing created heap
print ("The created heap is : ",end="")
print (list(li))


# In[4]:


# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)


# In[5]:


# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))


# In[6]:


# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))


# In[7]:


## 2nd example


# In[8]:


# initializing list 1
li1 = [5, 7, 9, 4, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)


# In[10]:


# using heappushpop() to push and pop items simultaneously
# pops 2
print ("The popped item using heappushpop() is : ",end="")
print (heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously
# In this, element is first popped, then the element is pushed.i.e, the value larger than the pushed value can be returned.
# pops 3
print ("The popped item using heapreplace() is : ",end="")
print (heapq.heapreplace(li2, 2))


# In[ ]:




