

import person_class

p1 = person_class.Person(12)
p1.get_population()
#1
print(p1.get_population())

p2 = person_class.Person(63)
p1.get_population()
#2
print(p1.get_population())

p2.get_population()
#2
print(p2.get_population())

p1.get_age()
#12
print(p1.get_age())

p2.get_age()
#63
print(p2.get_age())
