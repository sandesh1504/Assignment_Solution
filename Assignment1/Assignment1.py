#!/usr/bin/env python
# coding: utf-8

# In[4]:


d1 = {'a': 1, 'b': 2, 'c':3, 'd': 9}
d2 = {'a': 5, 'b': 6, 'c':7, 'e': 4} 

# get keys from one of the dictionary
d1_ks = [k for k in d1.keys()]
d2_ks = [k for k in d2.keys()]

all_ks = set(d1_ks + d2_ks)

print(all_ks)


# call values from each dictionary on available keys
d_merged = {k: [d1.get(k), d2.get(k)] for k in all_ks}

print(d_merged)


# In[ ]:




