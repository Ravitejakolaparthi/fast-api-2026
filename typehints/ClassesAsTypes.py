#########
#
#  Here we can send class as a type
# #
# class
class Person:
    
    def __init__(self,name: str):
        self.name = name
    def givename(self,):
        print(self.name)

# cit1 = Person("Raghu")
# cit1.givename()
###############

def get_person_name(one_person:Person):
    return one_person.givename()

citi = Person("Raja")
print(get_person_name(citi))