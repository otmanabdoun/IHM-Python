# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 03:41:59 2021

@author: User
"""

from lxml import etree

tree = etree.parse("data.xml")
for user in tree.xpath("/users/user[master='Master M2I']/nom"):
    print(user.text)