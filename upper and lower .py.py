#!/usr/bin/env python
# coding: utf-8

# In[49]:


def reverse_str(s):
    d={'UPPER_CASE':0} 
    l={'LOWER_CASE':0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           l["LOWER_CASE"]+=1
        else:
           continue
    print ("String:",s)
    print ("Upper case characters : ", d["UPPER_CASE"])
    print ("Lower case Characters : ", l["LOWER_CASE"])

reverse_str('The quick Brown Fox')


# In[ ]:




