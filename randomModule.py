import random

print(random.random()) #random value between 0 - 1 

print(random.randint(1,10))


list=[10,20,30,40,50,60]
print(random.choice(list)) #single 

print(random.sample(list,3)) #size 

print(list)
random.shuffle(list) # modify original list with random seq 
print(list)

