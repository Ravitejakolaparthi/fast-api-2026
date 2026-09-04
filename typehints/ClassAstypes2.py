class Person:
    def __init__(self,name:str,age:int,city:str):
        self.name = name
        self.age = age
        self.city = city
    def get_name(self,):
        return self.name
    def get_age(self,):
        return self.age
    def get_city(self,):
        return self.city

# Above is My class

# bot1 = Person("Alice",19,"Anakapalli")

# # Created an instance

# def get_details(person : Person): # Created a type 
#     return person.get_name(),person.get_age(),person.get_city()

# print(get_details(bot1))