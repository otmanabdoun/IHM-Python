# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:25:10 2021

@author: User
"""

import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
 'b': ('string', u'Unicode string'),
 'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

pickle.dump(data1, output)

pickle.dump(selfref_list, output, -1)

output.close()

