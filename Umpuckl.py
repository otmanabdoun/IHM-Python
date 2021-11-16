# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:29:06 2021

@author: User
"""

import pprint, pickle

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

pkl_file.close()
