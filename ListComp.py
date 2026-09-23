list = []

# 1 to 10 

for i in range(1,11):
    list.append(i)
print(list)

list = []    
list = [ x + 1 for x in range(0,10)]
print(list)


list = ["RoyAl","jaCK","SparroW","Denish","PatEl"]

result = [name.upper() for name in list]
print(result)

luckyWinner  = [name for name in list if len(name)%2 == 1]
print(luckyWinner)


luckyWinner  = [ (name,len(name)) for name in list if len(name)%2 == 1]
print(luckyWinner)


list = [11,-5,62,36,-9,100,500,0]
#neg pos 

result = [ "neg" if n  < 0  else "pos " for n in list]
print(result)

result = [ "post" if n  > 0  else "neg " if n < 0 else "zero" for n in list]
print(result)



list = ["RoyAl","jaCK","SparroW","Denish","PatEl"]

#reverse 


list = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]


result = [num  for row in list for num in row   ]


matrix  = [ [j for j in range(3)] for i in range (3)  ]

print(matrix)


numbers = [1,2,3,1,2,1,3,4,2,5,6]
#uniq numbers 



with open("data.txt","r")  as f:
    lines = [ line.stripe() for line in f]
    
    
with open("data.txt","r")  as f:
    words = [ line.stripe() for line in f if len(line.spripe() > 5 )]
    