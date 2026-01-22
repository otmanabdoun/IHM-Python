
from xml.etree import ElementTree
document = ElementTree.parse('data.xml')

users = document.find('users')

for user in document.findall('users/user'):
    print(user.attrib['data-id'])
    
    