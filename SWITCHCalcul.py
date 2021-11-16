class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

print("CALCULATOR".center(20, '-'))
a=int(input("Donner A : "))
b=int(input("Donner B : "))
op=input("Donner l'opérateur (+,-,*,/)  : ")
print("\nRésultats : ",end='\t')
while switch(op):
    if case('+'):
        print(a+b)
        break
    if case('-'):
        print(a-b)
        break
    if case('*'):
        print(a*b)
        break
    if case('/'):
        print(a/b)
        break
    print('Erreur! Opérateur inconuu !!!!')
    break

dir()