# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 03:33:58 2021

@author: User
"""

from lxml import etree


tree = etree.parse("data.xml")
for user in tree.xpath("/users/user"):
    print(user.get("data-id"))
    
    