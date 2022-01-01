# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 04:01:00 2021

@author: User
"""

from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

# <membership/>
membership = Element('membership')
# <membership><users/>
users = SubElement(membership, 'users')
# <membership><users><user/>
SubElement(users, 'user', name='john')
SubElement(users, 'user', name='charles')
SubElement(users, 'user', name='peter')
# <membership><groups/>
groups = SubElement(membership, 'groups')
# <membership><groups><group/>
group = SubElement(groups, 'group', name='users')
# <membership><groups><group><user/>
SubElement(group, 'user', name='john')
SubElement(group, 'user', name='charles')
# <membership><groups><group/>
group = SubElement(groups, 'group', name='administrators')
# <membership><groups><group><user/>
SubElement(group, 'user', name='peter')

output_file = open('membership.xml', 'w')
output_file.write('<?xml version="1.0"?>')
output_file.write(ElementTree.tostring(membership))
output_file.close()