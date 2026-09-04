from ClassAstypes2 import Person
bot1 = Person("Raya",21,"vizag")
def want_details(person :Person):
    return person.get_name(),person.get_age(),person.get_city()
print(want_details(bot1))