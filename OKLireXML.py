# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 01:35:54 2021

@author: User
"""

    
from lxml import etree

tree = etree.parse("data.xml")
for user in tree.xpath("/users/user/nom"):
    print(user.text)
