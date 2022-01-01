# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 04:06:39 2021

@author: User
"""

from xml.etree import ElementTree
document = ElementTree.parse('data.xml')

users = document.find('users')

for user in document.findall('users/user'):
    print(user.attrib['data-id'])
    
    