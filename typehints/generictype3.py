def exampletuple(item : tuple[int,int,str]):
    return item

print(exampletuple((10,20,"ramesh")))

def process(map : dict[int,int]):
    for i,j in map.items():
        print(i)
        print(j)
map ={
    1 : 1020,
    2 : 1400,
    3 : 1401
}
print(process(map))