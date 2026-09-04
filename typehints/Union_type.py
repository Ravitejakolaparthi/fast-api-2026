# For wether you dont know yet the type of it
# but sure it may be any of some types
# then we use union type
def Multitype(price : int|str):
    print(price)

# print(Multitype(100))

def Multi(thing : int|str|bytes|float):
    print(thing)

print(Multi(10.000))